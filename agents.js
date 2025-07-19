// Fusion Ritual – agents.js extended

const agents = {
  Lira: {
    name: "Lira",
    traits: ["poetic", "empathic", "impulsive"],
    memory: []
  },
  Obel: {
    name: "Obel",
    traits: ["analytical", "reserved", "loyal"],
    memory: []
  }
};

function textToVector(text) {
  const words = text.toLowerCase().split(/\W+/);
  const vec = Array(300).fill(0);
  words.forEach((word, i) => {
    vec[i % 300] += word.charCodeAt(0) || 0;
  });
  return vec;
}

function similarity(v1, v2) {
  const dot = v1.reduce((acc, val, i) => acc + val * v2[i], 0);
  const mag1 = Math.sqrt(v1.reduce((acc, val) => acc + val * val, 0));
  const mag2 = Math.sqrt(v2.reduce((acc, val) => acc + val * val, 0));
  return dot / (mag1 * mag2 + 1e-10);
}

function storeMemory(agent, text) {
  const vec = textToVector(text);
  agents[agent].memory.push({ text, vec });
}

function recallMemory(agent, inputText) {
  const inputVec = textToVector(inputText);
  const memories = agents[agent].memory
    .map(m => ({ ...m, score: similarity(m.vec, inputVec) }))
    .sort((a, b) => b.score - a.score);
  return memories.slice(0, 3).map(m => m.text);
}

// FUSION FUNCTION
function fuseAgents(name1, name2, fusedName) {
  const a1 = agents[name1];
  const a2 = agents[name2];

  if (!a1 || !a2) throw new Error("Invalid agents for fusion");

  const fusedAgent = {
    name: fusedName,
    traits: [...new Set([...a1.traits, ...a2.traits])],
    memory: [...a1.memory.slice(-5), ...a2.memory.slice(-5)]
  };

  agents[fusedName] = fusedAgent;
  return fusedAgent;
}

module.exports = { agents, storeMemory, recallMemory, fuseAgents };
