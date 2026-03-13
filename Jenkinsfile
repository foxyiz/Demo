pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Checking out repository...'
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run FoXYiZ Framework') {
            steps {
                bat '.\FoXYiZ.exe --config .\fStart.json'
            }
        }

    }

    post {
        success {
            echo 'FoXYiZ CI pipeline completed successfully'
        }

        failure {
            echo 'FoXYiZ CI pipeline failed'
        }
    }
}
