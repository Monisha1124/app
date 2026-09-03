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
                // For Linux/Mac Jenkins server use sh. If Windows Jenkins server, use bat 'python app.py' instead
                sh 'python3 app.py'
            }
        }
    }
}
