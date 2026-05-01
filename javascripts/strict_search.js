
document.addEventListener("DOMContentLoaded", () => {
    const targetNode = document.querySelector(".md-search-result");
    if (!targetNode) return;

    const observer = new MutationObserver(() => {
        const searchInput = document.querySelector(".md-search__input");
        if (!searchInput) return;

        const query = searchInput.value.trim().toLowerCase();
        // 取得所有關鍵字
        const keywords = query ? query.split(/\s+/) : [];

        const resultItems = document.querySelectorAll(".md-search-result__item");
        resultItems.forEach(item => {
            const article = item.querySelector(".md-search-result__article");
            if (!article) return;

            // 如果搜尋框是空的，確保所有東西都恢復原狀
            if (keywords.length === 0) {
                item.style.display = ""; 
                return;
            }

            // 檢查這部影片是否包含「所有」使用者打的字
            const text = article.textContent.toLowerCase();
            const isMatch = keywords.every(kw => text.includes(kw));

            if (!isMatch) {
                item.style.display = "none"; // 條件不符，隱藏
            } else {
                item.style.display = "";     // 🌟 關鍵修復：條件符合時，必須恢復顯示！
            }
        });
    });

    observer.observe(targetNode, { childList: true, subtree: true });
});
