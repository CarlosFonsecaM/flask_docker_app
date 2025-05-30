pipeline {
    agent any

    environment {
        IMAGE_NAME = "usuario/mi-app-flask"
        DOCKERHUB_CREDENTIALS = "dockerhub-creds"
    }

    stages {
        stage('Clonar repo') {
            steps {
                git url: 'https://github.com/usuario/flask-docker-app.git'
            }
        }

        stage('Construir imagen Docker') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Probar contenedor') {
            steps {
                sh 'docker run -d -p 5000:5000 --name app-prueba ${IMAGE_NAME}'
                sh 'sleep 5 && curl -f http://localhost:5000 || exit 1'
                sh 'docker stop app-prueba && docker rm app-prueba'
            }
        }

        stage('Publicar en Docker Hub') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry('', DOCKERHUB_CREDENTIALS) {
                        docker.image("${IMAGE_NAME}").push('latest')
                    }
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
        }
        failure {
            echo '❌ Falló el pipeline.'
        }
        success {
            echo '✅ Pipeline exitoso.'
        }
    }
}
