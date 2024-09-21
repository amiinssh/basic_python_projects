const minutesLabel = document.getElementById('minutes');
const secondsLabel = document.getElementById('seconds');
const milisecondsLabel = document.getElementById('miliseconds');

const startButton = document.getElementById('startBtn');
const stopButton = document.getElementById('stoptBtn');
const pauseButton = document.getElementById('pauseBtn');
const resetButton = document.getElementById('resetBtn');

const lapList = document.getElementById('laplist');

let minutes = 0;
let seconds = 0;
let miliseconds = 0;
let interval;

startButton.addEventListener('click', startTimer);
stopButton.addEventListener('click', stopTimer);
pauseButton.addEventListener('click', pauseTimer);
resetButton.addEventListener('click', resetTimer);

function startTimer(){

}

function stopTimer(){
    
}

function pauseTimer(){
    
}

function resetTimer(){
    
}

function updateTimer(){
    miliseconds++;
    if(miliseconds === 100){
        miliseconds = 0;
        seconds++;
        if(seconds === 60){
            seconds = 0;
            minutes++;
        }
    }

    displayTimer();
}

function displayTimer(){
    milisecondsLabel.textContent = miliseconds;
    secondsLabel.textContent = seconds;
    minutesLabel
}

