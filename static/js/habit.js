document.querySelector("#show-record-form".addEventListener("submit", (event) => {event.preventDefault();
    document.querySelector("#record_form").classList.remove("dn");
    document.querySelector("#show-record-form").classList.add("dn")
    document.querySelector("#id_qauntity").focus()
  });