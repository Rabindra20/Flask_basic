pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            // when {
            //     branch 'master'
            // }
            steps {
                // Checkout your source code
                checkout scm
                
                // Build Docker image
                script {
                    docker.build("rabindra/flask:${env.BUILD_NUMBER}")
                }
            }
            
        }
        stage('Push Docker Image') {
            // when {
            //     branch 'master'
            // }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_hub_login') {
                        // Push Docker image to Docker Hub
                        docker.image("rabindra/flask:${env.BUILD_NUMBER}").push()
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // def ip = ''
                    // def username = 'ubuntu'

                    // Use SSH agent credentials configured in Jenkins
                    // sshagent(credentials: ['ssh_cred']) {
                        // SSH into remote server and run Docker commands
                        sh """
                        // ssh -o StrictHostKeyChecking=no ${username}@${ip} '
                                docker stop flaskproject &&
                                docker rm flaskproject &&
                                docker run --pull always --restart always --name flaskproject -p 5000:5000 -d rabindra/flask:${env.BUILD_NUMBER}
                            // '
                        """
                    // }
                }
            }
        }
    }
}
