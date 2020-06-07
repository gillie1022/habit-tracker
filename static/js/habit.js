document
  .querySelector("#show_habit_form")
  .addEventListener("click", (event) => {
    event.preventDefault();
    document.querySelector("#record_form").classList.remove("dn");
  });