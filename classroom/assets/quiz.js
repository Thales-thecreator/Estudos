/* Quiz reutilizável das aulas da /teach.
   Uso: um elemento com data-quiz="ID" e, na mesma página, um script do tipo
   application/json com id="ID" contendo:
   {"score": true, "questions": [{"q": "...", "options": ["...", "..."], "answer": 0, "explain": "..."}]}
   Cada pergunta trava depois da primeira resposta e mostra o porquê na hora. */
(function () {
  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text != null) node.textContent = text;
    return node;
  }

  function render(container) {
    var source = document.getElementById(container.dataset.quiz);
    if (!source) return;
    var data = JSON.parse(source.textContent);
    var total = data.questions.length;
    var answered = 0;
    var right = 0;
    var score = null;

    data.questions.forEach(function (item, i) {
      var fs = el("fieldset", "q");
      var legend = el("legend");
      if (total > 1) legend.appendChild(el("span", "q-num", (i + 1) + "/" + total));
      legend.appendChild(document.createTextNode(item.q));
      fs.appendChild(legend);

      var options = el("div", "q-options");
      var feedback = el("p", "q-feedback");
      feedback.hidden = true;
      feedback.setAttribute("aria-live", "polite");

      item.options.forEach(function (text, j) {
        var btn = el("button", "q-option", text);
        btn.type = "button";
        btn.id = container.dataset.quiz + "-q" + i + "-o" + j;
        btn.addEventListener("click", function () {
          var buttons = options.querySelectorAll("button");
          buttons.forEach(function (b) { b.disabled = true; });
          var ok = j === item.answer;
          buttons[item.answer].classList.add("is-right");
          if (!ok) btn.classList.add("is-wrong");
          feedback.textContent = "";
          feedback.appendChild(el("span", "q-verdict", ok ? "Certo. " : "Errado. "));
          feedback.appendChild(document.createTextNode(item.explain));
          feedback.className = "q-feedback " + (ok ? "is-right" : "is-wrong");
          feedback.hidden = false;
          answered += 1;
          if (ok) right += 1;
          if (score) updateScore();
        });
        options.appendChild(btn);
      });

      fs.appendChild(options);
      fs.appendChild(feedback);
      container.appendChild(fs);
    });

    function updateScore() {
      if (answered < total) {
        score.textContent = "Respondidas: " + answered + " de " + total;
      } else {
        score.textContent = "Quiz feito: você acertou " + right + " de " + total + ".";
        score.classList.add("is-done");
      }
    }

    if (data.score) {
      score = el("p", "quiz-score");
      score.setAttribute("aria-live", "polite");
      container.appendChild(score);
      updateScore();
    }
  }

  document.querySelectorAll("[data-quiz]").forEach(render);
})();
