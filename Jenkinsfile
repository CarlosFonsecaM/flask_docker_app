pipeline {
    agent any
    
    environment{
        IMAGE_NAME = "carlosfonsecam/flask_docker_app"
        DOCKERHUB_CREDENTIALS = "dockerhub-creds"
    }
    
    stages{
        stage("Limpiar Workspace"){
            steps{
                script{
                    sh "rm -rf ./*"
                }
            }
        }
        stage("Clonar Repositorio"){
            steps{
                withCredentials([usernamePassword(credentialsId: 'GITHUB_CREDENTIALS', usernameVariable: "GITHUB_USERNAME", passwordVariable: "GITHUB_PASSWORD")]) {
                    script {
                        sh "git clone https://$GITHUB_USERNAME:$GITHUB_PASSWORD@github.com/CarlosFonsecaM/flask_docker_app.git"
                    }
                }
            }
        }
        
        stage("Construir imagen Docker"){
            steps{
                script{
                    sh "docker build -t ${IMAGE_NAME} flask_docker_app/"
                }
            }
        }
        stage("Probar Contenedor"){
            steps{
                script{
                    sh "docker run -d -p 5000:5000 --name app-prueba ${IMAGE_NAME}"
                    sh "sleep 5 && curl http://localhost:5000"
                    sh "docker stop app-prueba && docker rm app-prueba"
                }
            }
        }
        stage("Publicar en DockerHub"){
            steps{
                script{
                        docker.withRegistry('', DOCKERHUB_CREDENTIALS) {
                            docker.image("${IMAGE_NAME}").push('latest')
                        }
                }
            }
        }
    }
}
