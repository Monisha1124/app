pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Running Basic Python Application...'
                // Using 'bat' for Windows environment execution
                bat 'python app.py'
            }
        }
    }
}

