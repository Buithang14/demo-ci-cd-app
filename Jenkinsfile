pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Mức 1 - CI (Unit Test)') {
            steps {
                // Nếu Jenkins cài trực tiếp trên Windows, đổi 'sh' thành 'bat'
                sh 'pip install -r requirements.txt'
                sh 'pytest -v'
            }
        }
        stage('Mức 2 - CD (Build Docker)') {
            steps {
                // Nếu Jenkins cài trực tiếp trên Windows, đổi 'sh' thành 'bat'
                sh 'docker build -t demo-ci-cd-app:latest .'
            }
        }
    }
}