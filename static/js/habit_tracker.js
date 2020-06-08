document.querySelector("#show-record-form").addEventListener("click", (event) => {event.preventDefault();
    document.querySelector("#record-form").classList.remove("dn");
    document.querySelector("#show-record-form").classList.add("dn")
    document.querySelector("#id_quantity").focus()
})

// document.querySelector("#id_recorded_on").setAttribute("type", "date")