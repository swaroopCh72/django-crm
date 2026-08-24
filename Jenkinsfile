pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Django Checks') {
            steps {
                dir('CRMProject') {
                    sh 'python manage.py check'
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('CRMProject') {
                    sh 'python manage.py test'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t django-crm:latest .'
            }
        }
    }
}