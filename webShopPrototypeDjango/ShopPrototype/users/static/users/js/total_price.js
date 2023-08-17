document.addEventListener('DOMContentLoaded', function() {
    // Получение всех элементов с классом "history__item"
    const historyItems = document.querySelectorAll('.history__item');

    // Обход каждого элемента и выполнение операций
    historyItems.forEach((item) => {
        // Получение цены продукта из атрибута "data-product-price"
        const productPrice = item.dataset.productPrice;

        // Получение количества из элемента с классом "history__amount"
        const quantityElement = item.querySelector('.history__amount');
        const quantity = quantityElement.innerText.trim().split('\n')[1];
        const quantityInt = parseInt(quantity);

        // Проверка, является ли quantity числом
        if (!isNaN(quantityInt)) {
            // Вычисление общей стоимости
            console.log(productPrice)
            const totalPrice = parseFloat(productPrice) * parseFloat(quantityInt);
            const formattedTotalPrice = totalPrice.toFixed(2);

            // Вывод результата в элемент с классом "total-price"
            const totalPriceElement = item.querySelector('.history__total-price .total-price');
            totalPriceElement.textContent = formattedTotalPrice;
        }
    });
});
