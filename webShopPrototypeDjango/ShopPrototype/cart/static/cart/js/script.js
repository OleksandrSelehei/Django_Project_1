var dictionary = {}; // Создание словаря за пределами цикла
var TotalPrice = 0.00;

window.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.basket__card').forEach(function(card) {
    var minusBtn = card.querySelector('.basket-change__btn_minus');
    var plusBtn = card.querySelector('.basket-change__btn_plus');
    var input = card.querySelector('.basket-change__amount');
    var productId = card.getAttribute('data-product-id');

    var price = parseFloat(card.querySelector('.basket__card-price').textContent);
    dictionary[productId] = parseInt(input.value);
    TotalPrice += price * parseInt(input.value);

    minusBtn.addEventListener('click', function(e) {
      e.preventDefault();
      var value = parseInt(input.value);

      if (value > 1) {
        value = value - 1;
      } else {
        value = 1;
      }

      input.value = value;
      TotalPrice = TotalPrice - price;
      updateTotalPrice();

      dictionary[productId] = value;
    });

    plusBtn.addEventListener('click', function(e) {
      e.preventDefault();
      var value = parseInt(input.value);

      if (value < 100) {
        value = value + 1;
      } else {
        value = 100;
      }

      input.value = value;
      TotalPrice = TotalPrice + price;
      updateTotalPrice();

      dictionary[productId] = value;
    });
  });
});

function updateTotalPrice() {
  var totalPriceLabel = document.querySelector('.total_price label');
  if (totalPriceLabel) {
    totalPriceLabel.textContent = 'Total price: ' + TotalPrice.toFixed(2)  + '$';
  }
}

function updateDataCart(){
   $.ajax({
    url: '/cart/update_cart',
    type: 'POST',
    data: JSON.stringify(dictionary),
  });
}

function placeOrder() {
        updateDataCart();
        window.location.href = '/cart/order';
}

window.addEventListener('beforeunload', function(event) {
    updateDataCart();
});

