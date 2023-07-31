const newTransactionBtn = document.getElementById('new-transaction-btn');
const popupContainer = document.getElementById('popup-container');
const closePopupBtn = document.getElementById('close-popup-btn');

newTransactionBtn.addEventListener('click', function () {
  popupContainer.style.display = 'block';
});

closePopupBtn.addEventListener('click', function () {
  popupContainer.style.display = 'none';
});
