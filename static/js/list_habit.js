let deck = document.querySelectorAll(".habit-card")
for (let card of deck){
    let goal = parseInt(card.querySelector(".goal-quantity").textContent, 10)
    let quantity_list = card.querySelectorAll(".record-quantity")
    for (let value of quantity_list){
        let record_value = parseInt(value.textContent, 10);
        if (record_value >= goal) {value.textContent = "Y"}
        else if (record_value < goal) {value.textContent = "N"} 
        else {value.textContent = "U"}
    }
}