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

    interval = setInterval(updateTimer, 10);
    startButton.disabled = true; 

}

function stopTimer(){
    
    clearInterval(interval);
    addToLapList();
    resetTimerData();
    startButton.disabled = false;

}

function pauseTimer(){

    clearInterval(interval);
    startButton.disabled = false;
    
}

function resetTimer(){

    clearInterval(interval);
    resetTimerData();
    resetTimerData
    startButton.disabled = false;
    
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
    milisecondsLabel.textContent = padTime(miliseconds);
    secondsLabel.textContent = padTime(seconds);
    minutesLabel.textContent = padTime(minutes);
}

function padTime(time){
    return time.toString().padStart(2, '0');
}

function resetTimerData(){
    minutes = 0;
    seconds = 0;
    miliseconds = 0;
    displayTimer();
}

function addToLapList(){
    const lapTime = `${padTime(minutes)}:${padTime(seconds)}:${padTime(miliseconds)}`;
    const listItem = `<span>Lap ${lapList.childElementCount + 1}: <`;
}

