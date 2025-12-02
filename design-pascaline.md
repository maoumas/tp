<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Pascaline Simulator — Textured & Realistic</title>
  <style>
    /* --- Embedded textures via data‑URI --- */
    :root {
      --wood-url: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAF0lEQVR42mNgYGBg+M+AfwYGAAGKAC+d1pV0AAAAAElFTkSuQmCC");
      --brass-url: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAEElEQVQIW2NkYGBg+A8AAKkAArLm/DQAAAAASUVORK5CYII=");
    }

    body {
      margin: 0;
      padding: 20px;
      background: #5c4b37;
      display: flex;
      flex-direction: column;
      align-items: center;
      font-family: "Times New Roman", serif;
      color: #2b1f0e;
    }

    #machine {
      position: relative;
      background: var(--wood-url);
      background-size: 60px 60px;
      border: 6px solid #3a2b1d;
      border-radius: 12px;
      padding: 20px;
      box-shadow: inset 0 0 20px rgba(0,0,0,0.6), 0 5px 15px rgba(0,0,0,0.7);
      width: 600px;
      max-width: 95%;
    }

    #plate {
      position: relative;
      background: var(--brass-url);
      background-size: 40px 40px;
      border: 4px solid #4d3f2e;
      border-radius: 8px;
      padding: 20px;
      box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
    }

    .accumulator {
      display: flex;
      justify-content: center;
      margin-bottom: 20px;
      position: relative;
      height: 60px;
    }

    .acc-window {
      width: 50px;
      height: 60px;
      margin: 0 5px;
      background: #c9b58a;
      border: 3px solid #4d3f2e;
      border-radius: 6px;
      text-align: center;
      line-height: 60px;
      font-size: 1.6em;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.4);
      position: relative;
      color: #2b1f0e;
    }

    #compBar {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(60,50,40,0.8);
      display: none;
      border-radius: 6px;
      z-index: 2;
      pointer-events: none;
    }
    #compBar span {
      position: absolute;
      right: 8px;
      bottom: 6px;
      font-size: 0.8em;
      color: #e9e3d8;
      text-shadow: 1px 1px 2px rgba(0,0,0,0.7);
    }

    .input-wheels {
      display: flex;
      justify-content: center;
      margin-bottom: 10px;
    }

    .wheel {
      position: relative;
      width: 60px;
      height: 60px;
      margin: 0 6px;
      background: var(--brass-url);
      background-size: 40px 40px;
      border: 3px solid #4d3f2e;
      border-radius: 50%;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.5), 0 2px 4px rgba(0,0,0,0.6);
      cursor: pointer;
      user-select: none;
      overflow: hidden;
    }

    .wheel .digits {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      transition: transform 0.25s ease-out;
    }

    .wheel .digits div {
      height: 60px;
      line-height: 60px;
      text-align: center;
      font-size: 1.8em;
      color: #2b1f0e;
      font-family: serif;
    }

    /* Spokes overlay */
    .wheel::before {
      content: "";
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      border-radius: 50%;
      pointer-events: none;
      background:
        radial-gradient(circle at center, transparent 48%, rgba(0,0,0,0.3) 50%),
        repeating-linear-gradient( transparent 0 5%, rgba(0,0,0,0.3) 5% 6%, transparent 6% 11% );
      background-blend-mode: multiply;
    }

    .controls {
      text-align: center;
      margin: 10px 0 20px;
    }

    .controls button {
      background: #4d3f2e;
      color: #e9e3d8;
      border: none;
      padding: 10px 18px;
      margin: 0 5px;
      font-size: 1em;
      border-radius: 6px;
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(0,0,0,0.5);
    }

    .controls button:hover {
      background: #66543f;
    }

    .controls label {
      margin-left: 10px;
      font-size: 0.9em;
    }

    /* Educational section */
    .education {
      max-width: 600px;
      background: #ebe2d4;
      padding: 20px;
      border: 3px solid #4d3f2e;
      border-radius: 8px;
      box-shadow: inset 0 0 8px rgba(0,0,0,0.3);
      margin-top: 25px;
      color: #2b1f0e;
    }
    .education h2 {
      margin-top: 0;
      font-family: serif;
    }
  </style>
</head>
<body>

  <div id="machine">
    <div id="plate">
      <div class="accumulator" id="accumulator">
        <!-- accumulator windows will be generated here -->
        <div id="compBar"><span>9’s complement view</span></div>
      </div>

      <div class="input-wheels" id="inputWheels">
        <!-- input wheels generated here -->
      </div>

      <div class="controls">
        <button id="btnAdd">Enter / Add</button>
        <button id="btnClear">Clear (Reset)</button>
        <label><input type="checkbox" id="toggleComp"> Use 9’s‑complement (for subtraction)</label>
      </div>
    </div>
  </div>

  <div class="education">
    <h2>How it Works — Inside the Pascaline</h2>
    <p>
      Below the brass plate are the <strong>input dials (wheels)</strong>.  Each wheel is textured and shows radial spokes like a real crown wheel. Clicking a wheel simulates placing a stylus between spokes and rotating it one notch clockwise — the dial advances by one digit, and you cannot rotate backwards: this imitates the <strong>back‑stop pawl</strong> that prevents counter‑clockwise motion on the original Pascaline.
    </p>
    <p>
      Above sits the row of <strong>accumulator windows</strong> (output).  When you press “Enter / Add”, the values from the input wheels are added to the accumulator.  If a digit overflows from 9 → 0, a <strong>carry</strong> propagates to the next higher-order digit — this simulates the real Pascaline’s heavy lever + spring‑loaded pawl mechanism for carrying over automatically.  The carry ripple is handled internally by code.
    </p>
    <p>
      To perform <strong>subtraction</strong>, enable the “Use 9’s‑complement” checkbox.  Then dial the <strong>9’s‑complement of the number</strong> you wish to subtract, and press “Enter / Add.”  The accumulator will effectively subtract that number.  The sliding metal bar (semi‑transparent) toggles the display to show the complement digits — just as a hypothetical “complement view” overlay you might find on a mechanical calculator.
    </p>
    <p>
      The “Clear (Reset)” button simulates the mechanical reset method: internally sets all accumulator wheels to 9, then adds 1 to the lowest-order wheel, causing a ripple carry that resets all digits to 0 — just like resetting a real Pascaline.
    </p>
    <p style="font-style: italic; color: #4d3f2e;">
      Note: This is a visual and logical simulation.  The real machine would use crown wheels, pawls, levers, and metal gearwork — here, we approximate their effect via code, textures, and interaction constraints to evoke the 17th‑century feel.
    </p>
  </div>

  <script>
    const NUM = 6;
    let accumulator = new Array(NUM).fill(0);
    let input = new Array(NUM).fill(0);

    const accContainer = document.getElementById("accumulator");
    const inputWheelsContainer = document.getElementById("inputWheels");
    const compBar = document.getElementById("compBar");
    const toggleComp = document.getElementById("toggleComp");

    // build accumulator windows
    function buildAccumulator() {
      for (let i = 0; i < NUM; i++) {
        const w = document.createElement("div");
        w.className = "acc-window";
        w.textContent = "0";
        accContainer.appendChild(w);
      }
    }

    // build input wheels
    const wheelElems = [];
    function buildInputWheels() {
      for (let i = 0; i < NUM; i++) {
        const w = document.createElement("div");
        w.className = "wheel";
        const digits = document.createElement("div");
        digits.className = "digits";
        for (let d = 0; d < 10; d++) {
          const dd = document.createElement("div");
          dd.textContent = d;
          digits.appendChild(dd);
        }
        w.appendChild(digits);
        inputWheelsContainer.appendChild(w);
        wheelElems.push({ wheel: w, digits: digits });
        w.addEventListener("click", () => {
          rotateInput(i);
        });
      }
    }

    function rotateInput(idx) {
      input[idx] = (input[idx] + 1) % 10;
      const ds = wheelElems[idx].digits;
      ds.style.transform = `translateY(-${input[idx] * ds.children[0].offsetHeight}px)`;
    }

    function refreshAccumulatorDisplay(useComplement = false) {
      const wins = accContainer.querySelectorAll(".acc-window");
      for (let i = 0; i < NUM; i++) {
        const v = useComplement ? 9 - accumulator[i] : accumulator[i];
        wins[i].textContent = v;
      }
    }

    function addInputToAccumulator() {
      let carry = 0;
      for (let i = NUM - 1; i >= 0; i--) {
        const sum = accumulator[i] + input[i] + carry;
        accumulator[i] = sum % 10;
        carry = Math.floor(sum / 10);
      }
      refreshAccumulatorDisplay(false);
      resetInputWheels();
    }

    function resetInputWheels() {
      input.fill(0);
      wheelElems.forEach(w => {
        w.digits.style.transform = "translateY(0px)";
      });
    }

    function clearAccumulator() {
      accumulator = new Array(NUM).fill(9);
      refreshAccumulatorDisplay(false);
      setTimeout(() => {
        let carry = 1;
        for (let i = NUM - 1; i >= 0; i--) {
          const s = accumulator[i] + carry;
          accumulator[i] = s % 10;
          carry = Math.floor(s / 10);
        }
        refreshAccumulatorDisplay(false);
      }, 200);
    }

    function toggleComplementView() {
      const show = toggleComp.checked;
      compBar.style.display = show ? "block" : "none";
      refreshAccumulatorDisplay(show);
    }

    document.getElementById("btnAdd").addEventListener("click", () => {
      addInputToAccumulator();
      if (toggleComp.checked) {
        toggleComp.checked = false;
        toggleComplementView();
      }
    });
    document.getElementById("btnClear").addEventListener("click", clearAccumulator);
    toggleComp.addEventListener("change", toggleComplementView);

    // init
    buildAccumulator();
    buildInputWheels();
    refreshAccumulatorDisplay(false);
  </script>

</body>
</html>