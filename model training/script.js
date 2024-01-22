// set global - needed for external libraries
/* globals ml5 */

let message = document.querySelector("#message")
let myNeuralNetwork

function start() {
  
    const options = {
        dataUrl: './yoga.csv',
        inputs: ['leftAnklex','leftAnkley','leftEarx','leftEary','leftElbowx','leftElbowy','leftEyex','leftEyey','leftHipx','leftHipy','leftKneex','leftKneey','leftShoulderx','leftShouldery','leftWristx','leftWristy','nosex','nosey','rightAnklex','rightAnkley','rightEarx','rightEary','rightElbowx','rightElbowy','rightEyex','rightEyey','rightHipx','rightHipy','rightKneex','rightKneey','rightShoulderx','rightShouldery','rightWristx','rightWristy'],
        outputs: ['yogapose'],
        task: 'classification',
        debug: true
    }

  // uncomment to create the neural network
  myNeuralNetwork = ml5.neuralNetwork(options, dataLoaded)  
}

function dataLoaded() {
    message.innerHTML = "Finished loading - Start training"
  
    myNeuralNetwork.normalizeData()
    const trainingOptions = {
        epochs: 300,
        batchSize: 5
    }
    
     myNeuralNetwork.train(trainingOptions, finishedTraining)
}

function finishedTraining() {
    console.log("Finished training!")
    message.innerHTML = "Finished training"
  
    // to do: test if we can classify a new flower
    classify([543,161,567,136,519,133,609,148,483,155,651,302,451,308,710,494,382,498,806,659,302,641,610,652,488,654,615,928,508,927,611,1206,491,1200])
  
    // to do: save the model. in part 2 we will load the model
    // myNeuralNetwork.save()
}

function classify(input) {
    myNeuralNetwork.classify(input, handleResults)
}

function handleResults(error, result) {
    if (error) console.error(error)
    console.log(result[0].label + " confidence:" + result[0].confidence)
    message.innerHTML = result[0].label + " confidence:" + result[0].confidence
  
    console.log(result)
}


start()


// use these options for yoga training
/*
// options for yoga poses

*/