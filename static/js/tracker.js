document
  .querySelector("#show-record-form")
  .addEventListener("click", (event) => {
    event.preventDefault();
    document.querySelector("#record-form").classList.remove("dn");
    document.querySelector("#show-record-form").classList.add("dn");
    document.querySelector("#id_quantity").focus();
  });

records = document.querySelectorAll(".record");
for (let record of records) {
  record.addEventListener("click", (event) => {
    event.preventDefault();
    let form = record.parentElement.nextElementSibling;
    let qty = record.parentElement.parentElement.dataset.quantity;    
    form.classList.remove("dn");
    form.querySelector("input[name='quantity']").value = qty
  });
}
