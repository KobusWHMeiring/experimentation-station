document.addEventListener("DOMContentLoaded", function() {
    var dropdown = document.getElementById("model-type");
    dropdown.addEventListener("change", function() {
        if (dropdown.value === "question-answer") {
          document.getElementById("question-answer-container").classList.remove("hidden")
          document.getElementById("system-input").classList.remove("hidden")
          document.getElementById("templates-container").classList.remove("hidden") 
          document.getElementById("sentiment-analysis-container").classList.add("hidden")
        }
        else if(dropdown.value === "sentiment-analysis"){
            document.getElementById("question-answer-container").classList.add("hidden")
            document.getElementById("system-input").classList.add("hidden")
            document.getElementById("templates-container").classList.add("hidden")
            document.getElementById("sentiment-analysis-container").classList.remove("hidden")
        }
        else {
            document.getElementById("question-answer-container").classList.add("hidden")
            document.getElementById("system-input").classList.add("hidden")
            document.getElementById("templates-container").classList.add("hidden")
            document.getElementById("sentiment-analysis-container").classList.add("hidden")
        }
      });
})

function handleKeyDown(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    send();
  }
}




function sendUserMessage(prompt_content,system_prompt, model, template){
  
    displaySettings(model)
    let content = 
        {
            "prompt": prompt_content,
            "system_prompt": system_prompt,
            "model": model,
            "guid": guid,
            "template": template,
        }
    let config = 
        {
            type: "POST",
            url:  '/prompt/',
            data: content,
            dataType: 'json',
            success: displayResponseMessage
        };
        
    $.ajax(config);
}

function sendWhatsapp(message){
    console.log('Whatsapp message', message)
    displayResponseStatus()

    data = {
        "message":message,
    }
    let config = 
        {
            type: "POST",
            url:  '/whatsapp/',
            data: data,
            dataType: 'json',
            success: displayResponseStatus
        };
        
    $.ajax(config);
}

function send(){

    let prompt_content = document.getElementById("input").value
    let system_message = document.getElementById("system-input").value
    const radioButtons = document.querySelectorAll('input[name="format"]');
    let format;
            for (const radioButton of radioButtons) {
                if (radioButton.checked) {
                    format = radioButton.value;
                    break;
                }}

   

    let model_type = document.getElementById("model-type").value
    let template = document.getElementById("template").value
    let model = "gpt3.5"
    if(model_type == "question-answer"){
        model = document.getElementById("question-answer").value
    }
    else if(model_type === "sentiment-analysis"){
        model = document.getElementById("sentiment-analysis").value
    }

    
    document.getElementById("input").value = ""
    
    displayUserMessage(prompt_content)

    if (format == "whatsapp"){
        console.log('whatsapp if triggered')
        response = sendWhatsapp(prompt_content)
    }
    else{
        response = sendUserMessage(prompt_content, system_message, model, template)
    }   
}

var inputTextArea = document.getElementById("input");

inputTextArea.addEventListener("keydown", function (event) {
  if (event.ctrlKey && event.key == "Enter") {
    send();
  }
});

function displaySettings(model){
    model = "Selected Model: " + model
    let settings = document.createElement('div')
    settings.classList.add("settings-output")
    settings.innerHTML = model
    let settingsContainer = document.createElement('div')
    settingsContainer.classList.add("settings-output-container")
    settingsContainer.appendChild(settings)
    document.getElementById("output").appendChild(settingsContainer)
}

function displayResponseStatus(){
    
    stat = "success"
    console.log('Display response Status', stat)
    let statusIndicator = document.createElement('div')
    statusIndicator.classList.add("status-indicator")
    statusIndicator.innerHTML = stat
    let statusContainer = document.createElement('div')
    statusContainer.classList.add("status-indicator-container")
    statusContainer.appendChild(statusIndicator)
    console.log('statusContainer', statusContainer)
    document.getElementById("output").appendChild(statusContainer)
}

function displayResponseMessage(input){
    
    console.log('input', input)
    let newMessage = document.createElement("pre");
    newMessage.classList.add("response-message");
    newMessage.innerHTML = input.answer;
    console.log('newMessage', newMessage)

    let messageContainer = document.createElement("div");
    messageContainer.classList.add("user-message-container")
    messageContainer.appendChild(newMessage);
    console.log('messageContainer', messageContainer)

    let output = document.getElementById("output");
    console.log('output', output)
    output.appendChild(messageContainer);
}

function displayUserMessage(userMessage){
   
    let newMessage = document.createElement("p");
    newMessage.classList.add("user-message");
    newMessage.innerHTML = userMessage;
    let messageContainer = document.createElement("div");
    messageContainer.classList.add("user-message-container")
    messageContainer.appendChild(newMessage);
    let output = document.getElementById("output");
    output.appendChild(messageContainer);

}