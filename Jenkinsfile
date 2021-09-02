pipeline {
    agent { docker { image 'python:3.7.4' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
//         post{
//             always{
//                 //after all stages excuted
//             }
//             failure{
//             }
//         }
    }
}
