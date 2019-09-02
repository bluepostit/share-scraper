function fetchBrandShareData(searchTerm) {
  url = "/search?term=" + encodeURIComponent(searchTerm);
  return fetch(url)
  .then(response => response.json())
  .then((json) => {
    console.log(json);
  });
}

const setupFormListener = () => {
  document.querySelector('.search-form').addEventListener('submit', e => {
    e.preventDefault();
    const searchTerm = document.querySelector('#search-term').value;
    fetchBrandShareData(searchTerm);
  });
};

document.addEventListener("DOMContentLoaded", function(event) { 
  setupFormListener();
});