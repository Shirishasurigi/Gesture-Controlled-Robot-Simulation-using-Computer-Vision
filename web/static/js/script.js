async function updateGesture(){

    const response = await fetch("/gesture");

    const data = await response.json();

    document.getElementById("gesture").innerText =
        data.gesture;
}

setInterval(updateGesture,200);