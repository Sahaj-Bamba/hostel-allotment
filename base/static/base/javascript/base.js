window.addEventListener('visibilitychange',() => {
    if(document.hidden){
        console.log('Tab is hidden');
    }
    else{
        console.log('tab is focused');
    }
});

//      Ambient Light

window.addEventListener('devicelight',(e) => {
   console.log(e.value);
});


//          Battery Status

navigator.getBattery().then((battery) => {
   console.log(battery.level * 100);

    battery.addEventListener('levelchange',() => {
        console.log('this.level * 100');
    });
});
