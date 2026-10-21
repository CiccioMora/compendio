/**
 * APPLICAZIONE COMPENDIO MATERIE DI HOGWARTS
 * Gestione dello stato, filtri per anno e categoria, ricerca live e modale.
 */

document.addEventListener('DOMContentLoaded', () => {
  const data = window.materieData;
  if (!data) {
    console.error('materieData non caricato!');
    return;
  }

  // State
  let currentMacro = 'creature'; // 'creature' | 'piante' | 'pozioni'
  let currentYear = 'ALL';       // 'ALL' | 1..7
  let currentSecondary = 'ALL';  // Classificazione / Tipologia
  let searchQuery = '';

  // DOM Elements
  const searchInput = document.getElementById('searchInput');
  const clearSearchBtn = document.getElementById('clearSearchBtn');
  const macroTabs = document.querySelectorAll('.macro-tab');
  const yearFiltersContainer = document.getElementById('yearFiltersContainer');
  const secondaryFilterSelect = document.getElementById('secondaryFilterSelect');
  const secondaryFilterLabel = document.getElementById('secondaryFilterLabel');
  const cardsGrid = document.getElementById('cardsGrid');
  const resultsCountBadge = document.getElementById('resultsCountBadge');
  const activeFiltersCountBadge = document.getElementById('activeFiltersCountBadge');
  const resetFiltersBtn = document.getElementById('resetFiltersBtn');
  const noResultsState = document.getElementById('noResultsState');

  // Stats Counters
  const statCreature = document.getElementById('statCreature');
  const statPiante = document.getElementById('statPiante');
  const statPozioni = document.getElementById('statPozioni');
  const statTotal = document.getElementById('statTotal');

  if (statCreature) statCreature.textContent = data.creature.length;
  if (statPiante) statPiante.textContent = data.piante.length;
  if (statPozioni) statPozioni.textContent = data.pozioni.length;
  if (statTotal) statTotal.textContent = data.creature.length + data.piante.length + data.pozioni.length;

  // Modal Elements
  const itemModal = document.getElementById('itemModal');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const modalBackdrop = document.getElementById('modalBackdrop');
  const modalBadgeCategory = document.getElementById('modalBadgeCategory');
  const modalBadgeYear = document.getElementById('modalBadgeYear');
  const modalBadgeSpecial = document.getElementById('modalBadgeSpecial');
  const modalTitle = document.getElementById('modalTitle');
  const modalSubtitle = document.getElementById('modalSubtitle');
  const modalContentBody = document.getElementById('modalContentBody');

  // Year filter buttons
  const yearButtons = [
    { label: 'Tutti gli Anni', value: 'ALL' },
    { label: 'I Anno', value: '1' },
    { label: 'II Anno', value: '2' },
    { label: 'III Anno', value: '3' },
    { label: 'IV Anno', value: '4' },
    { label: 'V Anno', value: '5' },
    { label: 'VI Anno', value: '6' },
    { label: 'VII Anno', value: '7' }
  ];

  function renderYearButtons() {
    yearFiltersContainer.innerHTML = '';
    const currentDataset = data[currentMacro] || [];

    yearButtons.forEach(btnInfo => {
      const btn = document.createElement('button');
      btn.type = 'button';
      const isSelected = (currentYear === btnInfo.value);
      
      // Calculate count for this year in current macro
      let count = 0;
      if (btnInfo.value === 'ALL') {
        count = currentDataset.length;
      } else {
        count = currentDataset.filter(i => String(i.anno) === btnInfo.value).length;
      }

      btn.className = `year-filter-btn cursor-pointer px-3.5 py-1.5 rounded-full text-xs font-medium transition-all duration-200 border flex items-center gap-1.5 ${
        isSelected
          ? 'bg-amber-600 text-white border-amber-500 shadow-lg shadow-amber-600/30'
          : 'bg-slate-900/60 text-slate-300 border-slate-700/60 hover:border-amber-500/50 hover:text-white'
      }`;

      btn.innerHTML = `<span>${btnInfo.label}</span> <span class="text-[10px] px-1.5 py-0.5 rounded-full ${isSelected ? 'bg-amber-700 text-white' : 'bg-slate-800 text-amber-400'}">${count}</span>`;
      btn.addEventListener('click', () => {
        currentYear = btnInfo.value;
        renderYearButtons();
        applyFilters();
      });
      yearFiltersContainer.appendChild(btn);
    });
  }

  function updateSecondaryFilterOptions() {
    secondaryFilterSelect.innerHTML = '';
    currentSecondary = 'ALL';

    if (currentMacro === 'creature') {
      secondaryFilterLabel.textContent = 'Classificazione Ministeriale';
      const options = [
        { label: 'Tutte le Classi (X - XXXXX)', value: 'ALL' },
        { label: 'X — Noioso', value: 'X' },
        { label: 'XX — Innocuo / Addomesticabile', value: 'XX' },
        { label: 'XXX — Mago Capace', value: 'XXX' },
        { label: 'XXXX — Pericoloso / Specialista', value: 'XXXX' },
        { label: 'XXXXX — Noto Ammazzamaghi', value: 'XXXXX' }
      ];
      options.forEach(opt => {
        const el = document.createElement('option');
        el.value = opt.value;
        el.textContent = opt.label;
        secondaryFilterSelect.appendChild(el);
      });
    } else if (currentMacro === 'piante') {
      secondaryFilterLabel.textContent = 'Tipologia Botanica';
      const types = [
        { label: 'Tutte le Tipologie', value: 'ALL' },
        { label: 'Piante da Rimedio', value: 'Piante da Rimedio' },
        { label: 'Piante Velenose', value: 'Piante Velenose' },
        { label: 'Piante Antropomorfe', value: 'Piante Antropomorfe' },
        { label: 'Alteratrici di Stato', value: 'Alteratrici di Stato' },
        { label: 'Alberi Nobili & Legnami Magici', value: 'Alberi Nobili' },
        { label: 'Piante Maestre & Avanzate', value: 'Piante Maestre' },
        { label: 'Famiglia delle Fagiole', value: 'Fagiole' },
        { label: 'Strumentazione Magica', value: 'Strumentazione' },
        { label: 'Formule Botaniche', value: 'Formule Botaniche' },
        { label: 'Anatomia Botanica', value: 'Anatomia Botanica' },
        { label: 'Tecniche di Difesa & Bonifica', value: 'Bonifica' }
      ];
      types.forEach(opt => {
        const el = document.createElement('option');
        el.value = opt.value;
        el.textContent = opt.label;
        secondaryFilterSelect.appendChild(el);
      });
    } else if (currentMacro === 'pozioni') {
      secondaryFilterLabel.textContent = 'Tipologia Alchemica';
      const types = [
        { label: 'Tutte le Tipologie', value: 'ALL' },
        { label: 'Curativa / Medimagica', value: 'Curativa' },
        { label: 'Trasformante', value: 'Trasformante' },
        { label: 'Alteratrice di Stato', value: 'Alteratrice' },
        { label: 'Veleno / Tossico', value: 'Veleno' },
        { label: 'Antidoto', value: 'Antidoto' },
        { label: "Filtro d'Amore / Emotivo", value: 'Filtro' },
        { label: 'Elisir', value: 'Elisir' },
        { label: 'Sonnifero / Soporifera', value: 'Soporifera' },
        { label: 'Per Oggetti / Tattica', value: 'Oggetti' },
        { label: 'Cosmetica / Aspetto', value: 'Cosmetica' },
        { label: 'Veterinaria Magica', value: 'Veterinaria' },
        { label: 'Magia Oscura / Proibita', value: 'Oscura' }
      ];
      types.forEach(opt => {
        const el = document.createElement('option');
        el.value = opt.value;
        el.textContent = opt.label;
        secondaryFilterSelect.appendChild(el);
      });
    }
  }

  // Macro Tab Switching
  macroTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const selected = tab.getAttribute('data-macro');
      if (selected === currentMacro) return;
      currentMacro = selected;
      currentYear = 'ALL';
      searchQuery = '';
      searchInput.value = '';
      if (clearSearchBtn) clearSearchBtn.classList.add('hidden');

      macroTabs.forEach(t => {
        const isCurrent = t.getAttribute('data-macro') === currentMacro;
        t.setAttribute('aria-selected', isCurrent ? 'true' : 'false');
        if (isCurrent) {
          t.className = 'macro-tab active relative px-5 py-3 rounded-xl font-magic text-sm font-bold transition-all duration-300 flex items-center gap-2.5 shadow-lg bg-amber-600 text-white shadow-amber-600/30 border border-amber-500';
        } else {
          t.className = 'macro-tab relative px-5 py-3 rounded-xl font-magic text-sm font-bold transition-all duration-300 flex items-center gap-2.5 bg-slate-900/60 text-slate-400 hover:text-slate-200 border border-slate-800 hover:border-slate-700';
        }
      });

      updateSecondaryFilterOptions();
      renderYearButtons();
      applyFilters();
    });
  });

  // Filter application
  function applyFilters() {
    const dataset = data[currentMacro] || [];
    const query = searchQuery.trim().toLowerCase();

    const filtered = dataset.filter(item => {
      // Year filter
      if (currentYear !== 'ALL' && String(item.anno) !== currentYear) {
        return false;
      }

      // Secondary filter
      if (currentSecondary !== 'ALL') {
        if (currentMacro === 'creature') {
          if (item.classificazione !== currentSecondary) return false;
        } else if (currentMacro === 'piante') {
          if (!item.tipologia || !item.tipologia.toLowerCase().includes(currentSecondary.toLowerCase())) return false;
        } else if (currentMacro === 'pozioni') {
          const typeStr = (item.tipologia || '') + ' ' + (item.nomeAlternativo || '');
          if (!typeStr.toLowerCase().includes(currentSecondary.toLowerCase())) return false;
        }
      }

      // Search Query
      if (query) {
        const searchCorpus = [
          item.nome,
          item.nomeAlternativo,
          item.nomeBotanico,
          item.descrizione,
          item.habitat,
          item.tratti,
          item.proprieta,
          item.utilizziMagici,
          item.avvertenze,
          item.inventoreOrigine,
          ...(item.ingredienti || [])
        ].filter(Boolean).join(' ').toLowerCase();

        if (!searchCorpus.includes(query)) {
          return false;
        }
      }

      return true;
    });

    renderCards(filtered);

    // Update results badge
    let macroLabel = 'voci trovate';
    if (currentMacro === 'creature') macroLabel = 'creature trovate';
    else if (currentMacro === 'piante') macroLabel = 'specie & formule trovate';
    else if (currentMacro === 'pozioni') macroLabel = 'pozioni trovate';

    resultsCountBadge.textContent = `${filtered.length} ${macroLabel}`;

    // Active filters count
    let activeFiltersCount = 0;
    if (currentYear !== 'ALL') activeFiltersCount++;
    if (currentSecondary !== 'ALL') activeFiltersCount++;
    if (query) activeFiltersCount++;

    if (activeFiltersCount > 0) {
      activeFiltersCountBadge.textContent = `${activeFiltersCount} filtri attivi`;
      activeFiltersCountBadge.classList.remove('hidden');
      resetFiltersBtn.classList.remove('hidden');
    } else {
      activeFiltersCountBadge.classList.add('hidden');
      resetFiltersBtn.classList.add('hidden');
    }

    if (filtered.length === 0) {
      cardsGrid.classList.add('hidden');
      noResultsState.classList.remove('hidden');
      noResultsState.style.display = 'block';
    } else {
      cardsGrid.classList.remove('hidden');
      noResultsState.classList.add('hidden');
      noResultsState.style.display = 'none';
    }
  }

  // Render cards based on active macro
  function renderCards(items) {
    cardsGrid.innerHTML = '';

    items.forEach(item => {
      const card = document.createElement('div');
      card.className = 'glass-card rounded-2xl p-5 flex flex-col justify-between cursor-pointer border border-slate-800 hover:border-amber-500/40 transition-all duration-300';
      card.addEventListener('click', () => openModal(item));

      if (currentMacro === 'creature') {
        renderCreatureCard(card, item);
      } else if (currentMacro === 'piante') {
        renderPiantaCard(card, item);
      } else if (currentMacro === 'pozioni') {
        renderPozioneCard(card, item);
      }

      cardsGrid.appendChild(card);
    });
  }

  function renderCreatureCard(card, item) {
    let classColor = 'bg-slate-800 text-slate-300 border-slate-700';
    if (item.classificazione === 'X') classColor = 'bg-slate-800/80 text-slate-300 border-slate-700';
    else if (item.classificazione === 'XX') classColor = 'bg-emerald-950/70 text-emerald-300 border-emerald-800/60';
    else if (item.classificazione === 'XXX') classColor = 'bg-sky-950/70 text-sky-300 border-sky-800/60';
    else if (item.classificazione === 'XXXX') classColor = 'bg-purple-950/70 text-purple-300 border-purple-800/60';
    else if (item.classificazione === 'XXXXX') classColor = 'bg-rose-950/80 text-rose-300 border-rose-800/80 animate-pulse';

    card.innerHTML = `
      <div>
        <div class="flex items-center justify-between gap-2 mb-3">
          <span class="px-2.5 py-1 rounded-full text-[11px] font-semibold bg-amber-950/60 text-amber-300 border border-amber-800/60">
            ${item.annoLabel}
          </span>
          <span class="px-2.5 py-1 rounded-full text-[11px] font-bold border ${classColor}">
            Classe: ${item.classificazione}
          </span>
        </div>
        <h3 class="font-magic text-lg font-bold text-white mb-1 tracking-wide group-hover:text-amber-400 transition-colors">
          ${item.nome}
        </h3>
        <p class="text-xs text-amber-500/80 italic mb-2">${item.nomeAlternativo || 'Bestiario di Hogwarts'}</p>
        <p class="text-xs text-slate-400 line-clamp-3 mb-4 leading-relaxed">
          ${item.descrizione}
        </p>
      </div>
      <div>
        <div class="pt-3 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400">
          <span class="truncate max-w-[180px]"><i class="text-amber-500 mr-1">📍</i>${item.habitat || 'Globale'}</span>
          <span class="text-amber-400 font-medium hover:underline flex items-center gap-1">Scheda ➔</span>
        </div>
      </div>
    `;
  }

  function renderPiantaCard(card, item) {
    card.innerHTML = `
      <div>
        <div class="flex items-center justify-between gap-2 mb-3">
          <span class="px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-950/60 text-emerald-300 border border-emerald-800/60">
            ${item.annoLabel}
          </span>
          <span class="px-2 py-0.5 rounded text-[10px] font-medium bg-slate-800/80 text-slate-300 border border-slate-700 truncate max-w-[150px]">
            ${item.tipologia || 'Erbologia'}
          </span>
        </div>
        <h3 class="font-magic text-lg font-bold text-white mb-1 tracking-wide group-hover:text-emerald-400 transition-colors">
          ${item.nome}
        </h3>
        <p class="text-xs text-emerald-500/80 italic mb-2">${item.nomeBotanico || item.nomeAlternativo || 'Specie Botanica'}</p>
        <p class="text-xs text-slate-400 line-clamp-3 mb-4 leading-relaxed">
          ${item.descrizione}
        </p>
      </div>
      <div>
        <div class="pt-3 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400">
          <span class="truncate max-w-[180px]"><i class="text-emerald-500 mr-1">🌿</i>${item.partiUtilizzate ? item.partiUtilizzate.split(',')[0] : 'Tessuti vegetali'}</span>
          <span class="text-emerald-400 font-medium hover:underline flex items-center gap-1">Dettagli ➔</span>
        </div>
      </div>
    `;
  }

  function renderPozioneCard(card, item) {
    const ingCount = item.ingredienti ? item.ingredienti.length : 0;
    card.innerHTML = `
      <div>
        <div class="flex items-center justify-between gap-2 mb-3">
          <span class="px-2.5 py-1 rounded-full text-[11px] font-semibold bg-indigo-950/60 text-indigo-300 border border-indigo-800/60">
            ${item.annoLabel}
          </span>
          <span class="px-2 py-0.5 rounded text-[10px] font-medium bg-slate-800/80 text-amber-300 border border-slate-700 truncate max-w-[150px]">
            ${item.tipologia || 'Pozione'}
          </span>
        </div>
        <h3 class="font-magic text-lg font-bold text-white mb-1 tracking-wide group-hover:text-amber-400 transition-colors">
          ${item.nome}
        </h3>
        <p class="text-xs text-amber-500/80 italic mb-2">${item.nomeAlternativo || 'Manuale di Pozioni'}</p>
        <p class="text-xs text-slate-400 line-clamp-3 mb-3 leading-relaxed">
          ${item.descrizione}
        </p>
      </div>
      <div>
        <div class="pt-2 mb-2 flex items-center gap-2 text-[11px] text-slate-400">
          <span class="w-2.5 h-2.5 rounded-full bg-amber-500 shrink-0"></span>
          <span class="truncate">${item.coloreFinale || 'Trasparente'}</span>
        </div>
        <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400">
          <span>🧪 ${ingCount} ingredienti</span>
          <span class="text-amber-400 font-medium hover:underline flex items-center gap-1">Ricetta ➔</span>
        </div>
      </div>
    `;
  }

  // Open item modal with complete detailed layout
  function openModal(item) {
    modalTitle.textContent = item.nome;
    modalSubtitle.textContent = item.nomeAlternativo || item.nomeBotanico || '';
    modalBadgeYear.textContent = item.annoLabel;

    if (currentMacro === 'creature') {
      modalBadgeCategory.textContent = 'Creatura Magica';
      modalBadgeCategory.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-amber-950/80 text-amber-300 border border-amber-800';
      modalBadgeSpecial.textContent = `Classe ${item.classificazione} — ${item.classificazioneLabel}`;
      modalBadgeSpecial.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-purple-950/80 text-purple-300 border border-purple-800';

      modalContentBody.innerHTML = `
        <div class="space-y-4 text-sm text-slate-300 leading-relaxed">
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-amber-400 font-bold mb-1">Descrizione & Comportamento</h4>
            <p>${item.descrizione}</p>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div class="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
              <span class="text-amber-500 font-bold block mb-1">📍 Habitat & Diffusione</span>
              <p class="text-xs text-slate-300">${item.habitat || 'Sconosciuto'}</p>
            </div>
            <div class="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
              <span class="text-amber-500 font-bold block mb-1">🍖 Dieta & Nutrizione</span>
              <p class="text-xs text-slate-300">${item.dieta || 'Carnivoro / Onnivoro'}</p>
            </div>
          </div>
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-amber-400 font-bold mb-1">Utilizzi Magici & Alchemici</h4>
            <p class="text-xs text-slate-300">${item.utilizziMagici || 'Nessun utilizzo conosciuto.'}</p>
          </div>
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-amber-400 font-bold mb-1">Regolamentazione Ministeriale & Commercio</h4>
            <p class="text-xs text-slate-300">${item.regolamentazione || 'Norme ordinarie del Ministero della Magia.'}</p>
            <p class="text-[11px] text-amber-500 mt-2"><strong>Status Beni:</strong> ${item.commerciabilita || 'Non specificato'}</p>
          </div>
        </div>
      `;
    } else if (currentMacro === 'piante') {
      modalBadgeCategory.textContent = 'Erbologia & Botanica';
      modalBadgeCategory.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-emerald-950/80 text-emerald-300 border border-emerald-800';
      modalBadgeSpecial.textContent = item.tipologia || 'Specie Botanica';
      modalBadgeSpecial.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-teal-950/80 text-teal-300 border border-teal-800';

      modalContentBody.innerHTML = `
        <div class="space-y-4 text-sm text-slate-300 leading-relaxed">
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-emerald-400 font-bold mb-1">Profilo Botanico</h4>
            <p>${item.descrizione}</p>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div class="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
              <span class="text-emerald-500 font-bold block mb-1">🌿 Parti Utilizzate</span>
              <p class="text-xs text-slate-300">${item.partiUtilizzate || 'Fogliame, radici o frutti'}</p>
            </div>
            <div class="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
              <span class="text-emerald-500 font-bold block mb-1">✨ Proprietà Magiche</span>
              <p class="text-xs text-slate-300">${item.proprieta || 'Terapeutiche o trasmutative'}</p>
            </div>
          </div>
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-emerald-400 font-bold mb-1">Protocollo di Coltivazione & Cura</h4>
            <p class="text-xs text-slate-300">${item.coltivazioneCura || 'Coltivazione in serra a temperatura controllata.'}</p>
          </div>
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-emerald-400 font-bold mb-1">Applicazioni Pozionistiche & Medimagiche</h4>
            <p class="text-xs text-slate-300">${item.usiPozionistici || 'Ingrediente per pozioni e decotti officinali.'}</p>
          </div>
        </div>
      `;
    } else if (currentMacro === 'pozioni') {
      modalBadgeCategory.textContent = 'Pozione Avanzata';
      modalBadgeCategory.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-indigo-950/80 text-indigo-300 border border-indigo-800';
      modalBadgeSpecial.textContent = item.tipologia || 'Pozione';
      modalBadgeSpecial.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-amber-950/80 text-amber-300 border border-amber-800';

      const ingredientiList = (item.ingredienti || []).map(ing => `<li class="flex items-center gap-2"><span class="text-amber-500">✦</span> ${ing}</li>`).join('');
      const preparazioneList = (item.preparazione || []).map(step => `<li class="mb-1.5">${step}</li>`).join('');

      modalContentBody.innerHTML = `
        <div class="space-y-4 text-sm text-slate-300 leading-relaxed">
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-amber-400 font-bold mb-1">Descrizione & Effetti</h4>
            <p>${item.descrizione}</p>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
            <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
              <span class="text-amber-500 font-bold block">🎨 Colore Finale:</span>
              <span>${item.coloreFinale || 'Trasparente'}</span>
            </div>
            <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
              <span class="text-amber-500 font-bold block">⏱️ Tempo Stima:</span>
              <span>${item.tempoPreparazione || 'Non specificato'}</span>
            </div>
            <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
              <span class="text-amber-500 font-bold block">🥄 Assunzione:</span>
              <span>${item.metodoAssunzione || 'Ingestione'}</span>
            </div>
          </div>
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-amber-400 font-bold mb-2">Ingredienti Necessari</h4>
            <ul class="text-xs text-slate-300 space-y-1">
              ${ingredientiList || '<li>Nessun ingrediente elencato.</li>'}
            </ul>
          </div>
          <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <h4 class="font-magic text-amber-400 font-bold mb-2">Procedimento di Preparazione</h4>
            <ol class="text-xs text-slate-300 space-y-1.5 list-decimal pl-4">
              ${preparazioneList || '<li>Seguire le istruzioni del Maestro Pozionista.</li>'}
            </ol>
          </div>
          ${item.avvertenze ? `
          <div class="bg-amber-950/30 p-3.5 rounded-xl border border-amber-800/60">
            <h4 class="font-magic text-amber-400 font-bold mb-1">⚠️ Precauzioni & Avvertenze</h4>
            <p class="text-xs text-amber-200/90">${item.avvertenze}</p>
          </div>
          ` : ''}
          ${item.inventoreOrigine ? `
          <div class="text-[11px] text-slate-400 italic">
            <strong>Origine & Note Storiche:</strong> ${item.inventoreOrigine}
          </div>
          ` : ''}
        </div>
      `;
    }

    itemModal.style.display = 'flex';
    itemModal.classList.remove('hidden');
    itemModal.classList.add('active');
  }

  function closeModal() {
    itemModal.classList.remove('active');
    itemModal.classList.add('hidden');
    itemModal.style.display = 'none';
  }

  if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeModal);
  if (modalBackdrop) modalBackdrop.addEventListener('click', closeModal);
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && itemModal.classList.contains('active')) closeModal();
  });

  // Search input handler
  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value;
    if (clearSearchBtn) {
      if (searchQuery.length > 0) clearSearchBtn.classList.remove('hidden');
      else clearSearchBtn.classList.add('hidden');
    }
    applyFilters();
  });

  if (clearSearchBtn) {
    clearSearchBtn.addEventListener('click', () => {
      searchInput.value = '';
      searchQuery = '';
      clearSearchBtn.classList.add('hidden');
      applyFilters();
    });
  }

  // Secondary Filter Select
  secondaryFilterSelect.addEventListener('change', (e) => {
    currentSecondary = e.target.value;
    applyFilters();
  });

  // Reset all filters button
  resetFiltersBtn.addEventListener('click', () => {
    currentYear = 'ALL';
    currentSecondary = 'ALL';
    searchQuery = '';
    searchInput.value = '';
    if (clearSearchBtn) clearSearchBtn.classList.add('hidden');
    updateSecondaryFilterOptions();
    renderYearButtons();
    applyFilters();
  });

  // Initial setup
  updateSecondaryFilterOptions();
  renderYearButtons();
  applyFilters();
});
