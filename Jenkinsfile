pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Django Checks') {
            steps {
                dir('CRMProject') {
                    sh '../.venv/bin/python manage.py check'
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('CRMProject') {
                    sh '../.venv/bin/python manage.py test
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