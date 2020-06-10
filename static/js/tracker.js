document
  .querySelector("#show-record-form")
  .addEventListener("click", (event) => {
    event.preventDefault();
    document.querySelector("#record-form").classList.remove("dn");
    document.querySelector("#show-record-form").classList.add("dn");
    document.querySelector("#id_quantity").focus();
  });

// records = document.querySelectorAll(".record");
// for (let record of records) {
//   record.addEventListener("click", (event) => {
//     event.preventDefault();
//     record.parentElement.nextElementSibling.classList.remove("dn");
//   });
// }
