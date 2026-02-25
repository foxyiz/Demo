"""
Custom Actions Handler - For End Users

This file allows end users to add their own custom functions that can be used
in test plans. Simply add methods to the CustomActionHandler class below.

Usage in y2Actions.csv:
- ActionType: xCustom
- ActionName: your_method_name (without the 'x' prefix)
- Input: your input parameters (semicolon-separated if multiple)

Example:
    ActionType: xCustom
    ActionName: xMyCustomFunction
    Input: param1;param2;param3

The method should be named with 'x' prefix in this file:
    def xMyCustomFunction(self, aIn):
        # Your code here
        return "result"
"""

import logging
import os
import sys

# Import the base ActionHandler class
try:
    from x.xActions import ActionHandler
except ImportError:
    # Fallback for bundled execution
    x_dir = None
    try:
        x_dir = os.path.abspath(os.path.join(sys._MEIPASS, 'x'))  # type: ignore[attr-defined]
    except Exception:
        pass
    if not x_dir or not os.path.isdir(x_dir):
        x_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    if x_dir not in sys.path:
        sys.path.insert(0, x_dir)
    from xActions import ActionHandler  # type: ignore[import-not-found]

logger = logging.getLogger(__name__)


class CustomActionHandler(ActionHandler):
    """
    Custom Actions Handler - Add your own functions here.
    
    All methods should:
    1. Start with 'x' prefix (e.g., xMyFunction)
    2. Accept 'aIn' as the first parameter (input string, semicolon-separated)
    3. Return a string result
    4. Use self.validate_input(aIn) to get and validate input
    
    Example:
        def xMyCustomFunction(self, aIn):
            parts = self.validate_input(aIn).split(';')
            # Your logic here
            return "Success"
    """
    
    def __init__(self, timeout=6):
        super().__init__(timeout)
    
    # ============================================
    # ADD YOUR CUSTOM FUNCTIONS BELOW THIS LINE
    # ============================================
    
    def xExampleFunction(self, aIn):
        """
        Example custom function.
        
        Input format: "param1;param2"
        Returns: A string result
        """
        parts = self.validate_input(aIn).split(';')
        if len(parts) < 2:
            raise ValueError(f"Invalid input for xExampleFunction: {aIn}. Expected 'param1;param2'")
        
        param1 = parts[0].strip()
        param2 = parts[1].strip()
        
        logger.info(f"Example function called with: {param1}, {param2}")
        result = f"Processed: {param1} and {param2}"
        return result
    
    # Add more custom functions below as needed:
    # 
    # def xYourFunction(self, aIn):
    #     """Your function description."""
    #     parts = self.validate_input(aIn).split(';')
    #     # Your implementation here
    #     return "result"
    
    def xGetOAuthTokenForm(self, aIn):
        """
        Request an OAuth2 token using application/x-www-form-urlencoded body.

        Input format:
            token_url;client_id;client_secret;grant_type;[scope];[extra_params_json_or_query]

        - token_url (required) : token endpoint URL
        - client_id (required)  : client id (may be omitted if using other auth)
        - client_secret (required) : client secret (may be omitted if using other auth)
        - grant_type (required) : e.g. client_credentials, password, authorization_code
        - scope (optional)      : space-separated scopes
        - extra_params_json_or_query (optional) : JSON object string or query-string (k=v&k2=v2) for additional form params

        Returns:
            access_token string if present in JSON response, otherwise full JSON/text response.
        """
        import json
        try:
            import requests
        except Exception as e:
            raise ImportError("requests library is required for xGetOAuthTokenForm. Install with: pip install requests")

        parts = self.validate_input(aIn).split(';')
        if len(parts) < 4:
            raise ValueError("Invalid input for xGetOAuthTokenForm: expected token_url;client_id;client_secret;grant_type;[scope];[extra_params]")

        token_url = parts[0].strip()
        client_id = parts[1].strip()
        client_secret = parts[2].strip()
        grant_type = parts[3].strip()
        scope = parts[4].strip() if len(parts) >= 5 and parts[4].strip() else None
        extra = parts[5].strip() if len(parts) >= 6 and parts[5].strip() else None

        data = {'grant_type': grant_type}
        # Include client credentials in the form by default (some servers expect them in body)
        if client_id:
            data['client_id'] = client_id
        if client_secret:
            data['client_secret'] = client_secret
        if scope:
            data['scope'] = scope

        # Merge extra params if provided (JSON or query string)
        if extra:
            # Try JSON first
            try:
                extra_obj = json.loads(extra)
                if isinstance(extra_obj, dict):
                    data.update({k: str(v) for k, v in extra_obj.items()})
            except Exception:
                # Fallback: parse as query-string (k=v&k2=v2) or semicolon separated k=v
                try:
                    # Accept both & and ; as separators
                    for pair in [p for sep in ('&', ';') for p in extra.split(sep)]:
                        if '=' in pair:
                            k, v = pair.split('=', 1)
                            data[k.strip()] = v.strip()
                except Exception:
                    # If parsing fails, include raw extra under 'extra'
                    data['extra'] = extra

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        timeout = getattr(self, 'timeout', 6)
        try:
            resp = requests.post(token_url, data=data, headers=headers, timeout=timeout)
            text = resp.text
            if 200 <= resp.status_code < 300:
                # Try to return access_token if present
                try:
                    j = resp.json()
                    token = j.get('access_token') or j.get('token') or j.get('id_token')
                    return token if token else json.dumps(j)
                except Exception:
                    return text
            else:
                # Include response body for diagnostics
                raise Exception(f"Token request failed: {resp.status_code} {text}")
        except Exception as e:
            raise Exception(f"xGetOAuthTokenForm failed: {str(e)}")
