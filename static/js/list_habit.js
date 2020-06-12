let deck = document.querySelectorAll(".habit-card");

for (let card of deck) {
  let goal = parseInt(card.querySelector(".goal-quantity").textContent, 10);
  let quantity_list = card.querySelectorAll(".record-quantity");
  for (let value of quantity_list) {
    let record_value = parseInt(value.textContent, 10);
    if (record_value >= goal) {
      value.textContent = "";
      let Y_div = document.createElement("p");
      Y_div.classList.add("Y");
      Y_div.innerHTML = "<P>&#10003;</p>";
      value.replaceWith(Y_div);
    } else if (record_value < goal) {
      value.textContent = "";
      let X_div = document.createElement("p");
      X_div.classList.add("X");
      X_div.innerHTML = "<P>&#935;</p>";
      value.replaceWith(X_div);
    } else {
      value.textContent = "";
      value.classList.add("U");
      let U_div = document.createElement("p");
      U_div.classList.add("U");
      U_div.innerHTML = "<P>&#63;</p>";
      value.replaceWith(U_div);
    }
  }
}
