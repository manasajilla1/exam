pipeline{
    agent any
    stages{
        // stage("selenium"){
        //     steps{
        //         bat 'pip install -r requirements.txt'
        //         bat 'start /B python app.py'
        //         bat 'python -m pytest -v test_registration.py'
        //     }
        // }
        stage("build Image"){
            steps{
                bat 'docker build -t myselenium:v1 .'
            }
        }
        stage('Docker login'){
            steps{
                bat 'docker login -u ManasaJilla -p 11@manasa'
            }
        }
        stage('push into the docker hub'){
            steps{
                bat 'docker tag mycontainer manasajilla/myselenium:seleimage1'
                bat 'docker push manasajilla/myselenium:seleimage1'
            }
        }
        stage('deploy into kubernets'){
            steps{
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post{
        success{
            echo 'all test have passed'
        }
        failure{
            echo 'test cases has passed'
        }
    }
}
