# -*- coding: utf-8 -*-
"""
Builder per il Portale Materie (Clone per test di Creature, Piante e Pozioni).
Genera:
1. materieData.js (dataset completo di 263 voci)
2. materieApp.js (logica applicativa, filtri, ricerca, modale)
3. materie.html (interfaccia utente clone coerente con index.html)
"""

import sys, os, json
sys.path.append('scripts')
import data_creature, data_piante, data_pozioni

print("Caricamento dataset...")
creature = data_creature.creature_data
piante = data_piante.piante_data
pozioni = data_pozioni.pozioni_data

print(f"Creature: {len(creature)}, Piante: {len(piante)}, Pozioni: {len(pozioni)}")

# 1. GENERATE materieData.js
data_js = f"""/**
 * ARCHIVIO COMPENDIO MATERIE DI HOGWARTS
 * Dataset ufficiale per Creature Magiche, Erbologia Botanica e Pozioni Avanzate.
 * Tutte le voci sono suddivise per anno didattico (I - VII Anno), senza valenza.
 */

window.materieData = {{
  creature: {json.dumps(creature, ensure_ascii=False, indent=2)},
  piante: {json.dumps(piante, ensure_ascii=False, indent=2)},
  pozioni: {json.dumps(pozioni, ensure_ascii=False, indent=2)}
}};
"""

with open('materieData.js', 'w', encoding='utf-8') as f:
    f.write(data_js)
print("Generato con successo materieData.js")

# 2. GENERATE materieApp.js
app_js = """/**
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

  // Update Tab Badges dynamically
  macroTabs.forEach(t => {
    const macro = t.getAttribute('data-macro');
    const badge = t.querySelector('span.font-mono');
    if (badge && data[macro]) {
      badge.textContent = data[macro].length;
    }
  });

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
    { label: 'VII Anno', value: '7' },
    { label: 'Altri', value: '0' }
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
"""

with open('materieApp.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("Generato con successo materieApp.js")

# 3. GENERATE materie.html
html_content = """<!DOCTYPE html>
<html lang="it" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Compendio Arcano — Creature, Piante e Pozioni di Hogwarts</title>
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧪</text></svg>">
  <link rel="stylesheet" href="style.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            magic: {
              gold: '#d97706',
              amber: '#f59e0b',
              emerald: '#10b981',
              dark: '#0b0f17'
            }
          }
        }
      }
    }
  </script>
</head>
<body class="min-h-screen text-slate-200 antialiased selection:bg-amber-600 selection:text-white flex flex-col justify-between">

  <!-- Header Banner & Navigation -->
  <header class="border-b border-slate-800/80 bg-slate-950/70 backdrop-blur-md sticky top-0 z-40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-amber-600 via-emerald-600 to-indigo-700 p-0.5 shadow-lg shadow-amber-600/20">
          <div class="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center text-lg">
            🧪
          </div>
        </div>
        <div>
          <h1 class="font-magic text-lg font-bold text-white tracking-wider">Compendio Arcano delle Materie</h1>
          <p class="text-xs text-slate-400">Scuola di Magia e Stregoneria di Hogwarts</p>
        </div>
      </div>

      <!-- Quick Link to Spells Portal -->
      <div class="flex items-center gap-3">
        <a href="index.html" class="px-4 py-2 rounded-xl text-xs font-magic font-bold tracking-wide bg-slate-900 hover:bg-slate-800 text-amber-400 border border-amber-600/40 hover:border-amber-500 transition-all shadow-md flex items-center gap-2">
          <span>⚡ Portale Incantesimi & Rune</span>
          <span class="text-sm">➔</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8 pb-4 text-center">
    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-amber-950/60 text-amber-300 border border-amber-800/60 mb-4">
      <span>Archivio Ufficiale di Hogwarts</span>
      <span>•</span>
      <span>Cura Creature, Erbologia & Pozioni</span>
    </div>
    <h2 class="font-magic text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white tracking-tight mb-3">
      Trattato delle Discipline Magiche
    </h2>
    <p class="text-sm sm:text-base text-slate-400 max-w-2xl mx-auto leading-relaxed">
      Esplora l'enciclopedia interattiva dedicata alle bestie magiche del Ministero, alle colture botaniche delle serre e alle preparazioni alchemiche di Libatius Borage.
    </p>

    <!-- Global Stats Overview -->
    <div class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-3xl mx-auto">
      <div class="glass-panel rounded-xl p-3 text-center border border-slate-800">
        <span class="text-xs text-slate-400 block mb-0.5">🐉 Creature Magiche</span>
        <span id="statCreature" class="font-magic text-xl font-bold text-amber-400">74</span>
      </div>
      <div class="glass-panel rounded-xl p-3 text-center border border-slate-800">
        <span class="text-xs text-slate-400 block mb-0.5">🌿 Erbologia & Piante</span>
        <span id="statPiante" class="font-magic text-xl font-bold text-emerald-400">57</span>
      </div>
      <div class="glass-panel rounded-xl p-3 text-center border border-slate-800">
        <span class="text-xs text-slate-400 block mb-0.5">🧪 Pozioni Avanzate</span>
        <span id="statPozioni" class="font-magic text-xl font-bold text-indigo-400">137</span>
      </div>
      <div class="glass-panel rounded-xl p-3 text-center border border-slate-800">
        <span class="text-xs text-slate-400 block mb-0.5">📚 Totale Voci</span>
        <span id="statTotal" class="font-magic text-xl font-bold text-white">268</span>
      </div>
    </div>
  </section>

  <!-- Controls, Tabs & Filters Section -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 w-full flex-grow">
    
    <!-- Macro Category Tabs -->
    <div class="flex items-center justify-center gap-2 sm:gap-4 mb-6 border-b border-slate-800/80 pb-5">
      <button type="button" data-macro="creature" aria-selected="true" class="macro-tab active relative px-5 py-3 rounded-xl font-magic text-sm font-bold transition-all duration-300 flex items-center gap-2.5 shadow-lg bg-amber-600 text-white shadow-amber-600/30 border border-amber-500">
        <span class="text-lg">🐉</span>
        <span>Creature Magiche</span>
        <span class="text-[11px] px-2 py-0.5 rounded-full bg-amber-700 text-white font-mono">74</span>
      </button>

      <button type="button" data-macro="piante" aria-selected="false" class="macro-tab relative px-5 py-3 rounded-xl font-magic text-sm font-bold transition-all duration-300 flex items-center gap-2.5 bg-slate-900/60 text-slate-400 hover:text-slate-200 border border-slate-800 hover:border-slate-700">
        <span class="text-lg">🌿</span>
        <span>Erbologia & Piante</span>
        <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-300 font-mono">57</span>
      </button>

      <button type="button" data-macro="pozioni" aria-selected="false" class="macro-tab relative px-5 py-3 rounded-xl font-magic text-sm font-bold transition-all duration-300 flex items-center gap-2.5 bg-slate-900/60 text-slate-400 hover:text-slate-200 border border-slate-800 hover:border-slate-700">
        <span class="text-lg">🧪</span>
        <span>Arte delle Pozioni</span>
        <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-300 font-mono">137</span>
      </button>
    </div>

    <!-- Search & Active Filters Bar -->
    <div class="glass-panel rounded-2xl p-4 sm:p-5 mb-6 border border-slate-800/80 shadow-xl">
      <div class="flex flex-col md:flex-row gap-4 items-stretch md:items-center justify-between mb-4">
        <!-- Live Search Input -->
        <div class="relative flex-grow">
          <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
          <input 
            type="text" 
            id="searchInput" 
            placeholder="Cerca per nome, ingredienti, classificazione, habitat o effetti..." 
            class="w-full pl-10 pr-10 py-2.5 rounded-xl bg-slate-950/80 border border-slate-700/80 text-white placeholder-slate-500 text-sm focus:outline-none focus:border-amber-500 focus:ring-1 focus:ring-amber-500 transition-all font-sans"
          />
          <button type="button" id="clearSearchBtn" class="hidden absolute inset-y-0 right-0 pr-3 flex items-center text-slate-400 hover:text-white">
            ✕
          </button>
        </div>

        <!-- Secondary Filter Dropdown (Custom per macro-category, NO valenza) -->
        <div class="flex items-center gap-2 shrink-0">
          <label id="secondaryFilterLabel" for="secondaryFilterSelect" class="text-xs font-semibold text-slate-400 whitespace-nowrap">
            Filtro Specifico:
          </label>
          <select id="secondaryFilterSelect" class="px-3 py-2 rounded-xl bg-slate-950/80 border border-slate-700/80 text-white text-xs focus:outline-none focus:border-amber-500">
            <!-- Populated dynamically via JS -->
          </select>
        </div>
      </div>

      <!-- Year Buttons (Common to all 3 categories) -->
      <div>
        <span class="text-xs font-semibold text-slate-400 block mb-2">Anno di Corso Didattico:</span>
        <div id="yearFiltersContainer" class="flex flex-wrap gap-2">
          <!-- Populated dynamically via JS -->
        </div>
      </div>

      <!-- Active Filters Status Bar -->
      <div class="mt-4 pt-3 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3 text-xs">
        <div class="flex items-center gap-2">
          <span id="resultsCountBadge" class="font-bold text-amber-400">0 voci trovate</span>
          <span id="activeFiltersCountBadge" class="hidden px-2 py-0.5 rounded-full bg-amber-950/80 text-amber-300 border border-amber-800 text-[11px]"></span>
        </div>
        <button type="button" id="resetFiltersBtn" class="hidden text-slate-400 hover:text-amber-400 underline transition-colors">
          Resetta tutti i filtri
        </button>
      </div>
    </div>

    <!-- Cards Grid -->
    <div id="cardsGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
      <!-- Populated dynamically via JS -->
    </div>

    <!-- Empty State -->
    <div id="noResultsState" class="hidden py-16 text-center">
      <div class="w-16 h-16 mx-auto mb-4 rounded-2xl bg-slate-900 border border-slate-800 flex items-center justify-center text-3xl">
        🔍
      </div>
      <h3 class="font-magic text-xl font-bold text-white mb-2">Nessun elemento trovato</h3>
      <p class="text-sm text-slate-400 max-w-md mx-auto">
        Nessuna voce corrisponde ai parametri di ricerca selezionati. Prova a reimpostare i filtri o la query di ricerca.
      </p>
    </div>

  </main>

  <!-- Detailed Modal Popup -->
  <div id="itemModal" style="display: none;" class="fixed inset-0 z-50 flex items-center justify-center p-4 hidden transition-opacity duration-200">
    <div id="modalBackdrop" class="fixed inset-0 bg-black/80 backdrop-blur-sm transition-opacity cursor-pointer"></div>
    <div class="glass-panel relative w-full max-w-2xl max-h-[85vh] overflow-y-auto rounded-3xl border border-slate-700 shadow-2xl p-6 sm:p-7 z-10 flex flex-col justify-between">
      <div>
        <div class="flex items-start justify-between gap-4 mb-3">
          <div class="flex flex-wrap items-center gap-2">
            <span id="modalBadgeCategory" class="px-3 py-1 rounded-full text-xs font-semibold bg-amber-950/80 text-amber-300 border border-amber-800">
              Categoria
            </span>
            <span id="modalBadgeYear" class="px-3 py-1 rounded-full text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700">
              Anno
            </span>
            <span id="modalBadgeSpecial" class="px-3 py-1 rounded-full text-xs font-semibold bg-purple-950/80 text-purple-300 border border-purple-800">
              Speciale
            </span>
          </div>
          <button type="button" id="modalCloseBtn" class="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition-colors">
            ✕
          </button>
        </div>

        <h3 id="modalTitle" class="font-magic text-2xl font-bold text-white mb-1 tracking-wide">
          Titolo Elemento
        </h3>
        <p id="modalSubtitle" class="text-xs text-amber-500 italic mb-5">
          Sottotitolo / Sinonimi
        </p>

        <div id="modalContentBody">
          <!-- Populated dynamically via JS -->
        </div>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="border-t border-slate-800/80 bg-slate-950/80 py-6 text-center text-xs text-slate-500">
    <div class="max-w-7xl mx-auto px-4">
      <p class="font-magic text-slate-400 mb-1">Archivio Accademico di Hogwarts • Anno Didattico Ufficiale</p>
      <p>Creature Magiche (Martina Mills) • Manuale di Erbologia • Advanced Potion Making (Libatius Borage)</p>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="materieData.js"></script>
  <script src="materieApp.js"></script>
</body>
</html>
"""

with open('materie.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("Generato con successo materie.html")

# 4. GENERATE dist/materie_standalone.html AND ARTIFACT
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

standalone_html = html_content
standalone_html = standalone_html.replace(
    '<link rel="stylesheet" href="style.css">',
    f'<style>\n{css_content}\n</style>'
)
standalone_html = standalone_html.replace(
    '<script src="materieData.js"></script>',
    f'<script>\n{data_js}\n</script>'
)
standalone_html = standalone_html.replace(
    '<script src="materieApp.js"></script>',
    f'<script>\n{app_js}\n</script>'
)

os.makedirs('dist', exist_ok=True)
with open('dist/materie_standalone.html', 'w', encoding='utf-8') as f:
    f.write(standalone_html)
print("Generato con successo dist/materie_standalone.html")

artifact_path = '/Users/andreamorachioli/.gemini/antigravity/brain/3a4f7fa7-8206-4f51-b303-aa9b9d9eaf5c/materie.html'
if os.path.exists(os.path.dirname(artifact_path)):
    with open(artifact_path, 'w', encoding='utf-8') as f:
        f.write(standalone_html)
    print(f"Aggiornato con successo l'artifact {artifact_path}")

print("Tutti i file del Portale Materie sono stati compilati ed esportati con successo!")
