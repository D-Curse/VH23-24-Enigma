const animalImage = document.getElementById('image');
const guessForm = document.getElementById('mcq-form');
const resultDiv = document.getElementById('result');
const submitButton = document.getElementById('submit');

const animals = [
    { image: 'Clause1.jpg', question: 'What animal is shown in this image?', options: ['Lion', 'Elephant', 'Giraffe', 'Penguin'], correctAnswer: 'Lion' },
    // Add more questions and images here
];

let currentQuestionIndex = 0;

// Initialize the game
loadQuestion(currentQuestionIndex);

// Function to load a question
function loadQuestion(index) {
    const currentQuestion = animals[index];
    animalImage.src = currentQuestion.image;
    document.querySelector('.question p').textContent = currentQuestion.question;
    
    const optionsContainer = document.querySelector('.options');
    optionsContainer.innerHTML = '';
    
    currentQuestion.options.forEach((option) => {
        const button = document.createElement('button');
        button.textContent = option;
        button.addEventListener('click', () => checkAnswer(option));
        optionsContainer.appendChild(button);
    });
}

// Function to check the answer
function checkAnswer(selectedAnswer) {
    const currentQuestion = animals[currentQuestionIndex];
    if (selectedAnswer === currentQuestion.correctAnswer) {
        resultDiv.textContent = 'Correct! It is a ' + currentQuestion.correctAnswer + '.';
        resultDiv.style.color = 'green';
    } else {
        resultDiv.textContent = 'Incorrect. It is not a ' + selectedAnswer + '.';
        resultDiv.style.color = 'red';
        animalImage.classList.add('shake');

        // Remove the shake class after a short delay (e.g., 1 second)
        setTimeout(() => {
            animalImage.classList.remove('shake');
        }, 800);;
    }
    
    // Increment the question index
    currentQuestionIndex++;
    
    // Clear the options and result after a short delay
    setTimeout(() => {
        if (currentQuestionIndex < animals.length) {
            loadQuestion(currentQuestionIndex);
            resultDiv.textContent = '';
        } else {
            resultDiv.textContent = 'Game Over! You have completed the game.';
        }
    }, 800); // Delay of 2 seconds (2000 milliseconds)
}

// Prevent the form from submitting
guessForm.addEventListener('submit', (e) => {
    e.preventDefault();
});