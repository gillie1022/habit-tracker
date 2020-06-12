let records = document.querySelectorAll(".record");
for (let record of records) {
  record.addEventListener("click", (event) => {
    event.preventDefault();
    let form = record.parentElement.nextElementSibling;
    let qty = record.parentElement.parentElement.dataset.quantity;    
    form.classList.remove("dn");
    form.classList.add("form")
    form.querySelector("input[name='quantity']").value = qty
    form.querySelector("input[name='quantity']").focus()
  });
}
