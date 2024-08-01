const chatbotToggler = document.querySelector(".chatbot-toggler");
const closeBtn = document.querySelector(".close-btn");
const chatbox = document.querySelector(".chatbox");
const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");

let userMessage = null; // Variable to store user's message
const inputInitHeight = chatInput.scrollHeight;

// API configuration
const API_URL = `http://localhost:5000/`;

const createChatLi = (message, className) => {
    // Create a chat <li> element with passed message and className
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", `${className}`);
    let chatContent =
        className === "human"
            ? `<p></p>`
            : `<span class="material-symbols-outlined">smart_toy</span><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi; // return chat <li> element
};

const generateResponse = async (chatElement) => {
    const messageElement = chatElement.querySelector("p");

    // Define the properties and message for the API request
    const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ role: "human", msg: userMessage }),
    };

    fetch("/process-data", requestOptions)
        .then((response) => response.json())
        .then((result) => {
            // Get the API response text and update the message element
            messageElement.textContent = result.msg;
        })
        .catch((error) => {
            // Handle error
            messageElement.classList.add("error");
            messageElement.textContent =
                "Oops!\nSomething went wrong.\nPlease try again.";
        })
        .finally(() => {
            chatbox.scrollTo(0, chatbox.scrollHeight);
        });

    // // Send POST request to API, get response and set the response as paragraph text
    // try {
    //     const response = await fetch(API_URL, requestOptions);
    //     console.log(response);
    //     const data = await response.json();
    //     console.log(data);
    //     if (!response.ok) throw new Error(data.error.message);

    //     // Get the API response text and update the message element
    //     messageElement.textContent =
    //         data.candidates[0].content.parts[0].text.replace(
    //             /\*\*(.*?)\*\*/g,
    //             "$1"
    //         );
    // } catch (error) {
    //     // Handle error
    //     messageElement.classList.add("error");
    //     messageElement.textContent = error.message;
    // } finally {
    //     chatbox.scrollTo(0, chatbox.scrollHeight);
    // }
};

const handleChat = () => {
    userMessage = chatInput.value.trim(); // Get user entered message and remove extra whitespace
    if (!userMessage) return;

    // Clear the input textarea and set its height to default
    chatInput.value = "";
    chatInput.style.height = `${inputInitHeight}px`;

    // Append the user's message to the chatbox
    chatbox.appendChild(createChatLi(userMessage, "human"));
    chatbox.scrollTo(0, chatbox.scrollHeight);

    setTimeout(() => {
        // Display "Thinking..." message while waiting for the response
        const aiChatLi = createChatLi("Thinking...", "ai");
        chatbox.appendChild(aiChatLi);
        chatbox.scrollTo(0, chatbox.scrollHeight);
        generateResponse(aiChatLi);
    }, 600);
};

chatInput.addEventListener("input", () => {
    // Adjust the height of the input textarea based on its content
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (e) => {
    // If Enter key is pressed without Shift key and the window
    // width is greater than 800px, handle the chat
    if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
    }
});

sendChatBtn.addEventListener("click", handleChat);
closeBtn.addEventListener("click", () =>
    document.body.classList.remove("show-chatbot")
);
chatbotToggler.addEventListener("click", () =>
    document.body.classList.toggle("show-chatbot")
);
