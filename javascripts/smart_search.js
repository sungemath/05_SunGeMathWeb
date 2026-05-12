
document.addEventListener("DOMContentLoaded", () => {
    const targetNode = document.querySelector(".md-search-result");
    if (!targetNode) return;

    let lastResultCount = 0;

    const observer = new MutationObserver(() => {
        const searchInput = document.querySelector(".md-search__input");
        if (!searchInput) return;

        const rawQuery = searchInput.value.trim();
        const isExactMatch = rawQuery.startsWith('"') && rawQuery.endsWith('"') && rawQuery.length > 2;
        const exactPhrase = isExactMatch ? rawQuery.slice(1, -1).toLowerCase() : "";

        const resultItems = document.querySelectorAll(".md-search-result__item");

        if (isExactMatch) {
            resultItems.forEach(item => {
                const link = item.querySelector("a.md-search-result__link");
                if (!link) return;

                const contentText = item.textContent.toLowerCase();
                const urlText = decodeURIComponent(link.getAttribute("href") || "").toLowerCase();
                
                if (contentText.includes(exactPhrase) || urlText.includes(exactPhrase.replace(/[\[\]]/g, ""))) {
                    item.style.display = "";
                } else {
                    item.style.display = "none";
                }
            });

            const scrollContainer = document.querySelector(".md-search-result__list");
            if (scrollContainer && resultItems.length > lastResultCount) {
                lastResultCount = resultItems.length;
                scrollContainer.scrollTop = scrollContainer.scrollHeight;
            }
        } else {
            resultItems.forEach(item => item.style.display = "");
            lastResultCount = 0;
        }
    });

    observer.observe(targetNode, { childList: true, subtree: true });
});
