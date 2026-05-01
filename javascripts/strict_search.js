
document.addEventListener("DOMContentLoaded", () => {
    const targetNode = document.querySelector(".md-search-result");
    if (!targetNode) return;

    const observer = new MutationObserver(() => {
        const searchInput = document.querySelector(".md-search__input");
        if (!searchInput) return;

        const query = searchInput.value.trim().toLowerCase();
        if (!query) return;

        // 將使用者的輸入用「空白鍵」切開，變成多個嚴格條件
        const keywords = query.split(/\s+/);

        const resultItems = document.querySelectorAll(".md-search-result__item");
        resultItems.forEach(item => {
            const article = item.querySelector(".md-search-result__article");
            if (!article) return;

            // 檢查這部影片的真實標題與內容，是否包含「所有」使用者打的字！
            const text = article.textContent.toLowerCase();
            const isMatch = keywords.every(kw => text.includes(kw));

            if (!isMatch) {
                // 如果不符合嚴格條件，直接隱藏！
                item.style.cssText = "display: none !important;";
            }
        });
    });

    observer.observe(targetNode, { childList: true, subtree: true });
});
