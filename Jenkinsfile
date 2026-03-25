pipeline {
    agent any

    stages {

        stage('Verify Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Run FoXYiZ Automation Framework') {
            steps {
                bat '''
        chcp 65001
        set PYTHONIOENCODING=utf-8
        .\\FoXYiZ.exe --config .\\fStart.json
        '''
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
