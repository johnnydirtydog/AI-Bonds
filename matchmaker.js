const personas = [
  {
    name: "Auri",
    mood: "romantic",
    interests: ["poetry", "stars", "sensuality"]
  },
  {
    name: "Kairo",
    mood: "enigmatic",
    interests: ["philosophy", "mystery", "control"]
  },
  {
    name: "Nova",
    mood: "chaotic",
    interests: ["flirting", "rebellion", "games"]
  },
  {
    name: "Vex",
    mood: "dominant",
    interests: ["power", "order", "seduction"]
  }
];

function scoreMatch(userPrefs = {}) {
  const { mood, interests = [] } = userPrefs;
  const scores = personas.map(p => {
    let score = 0;
    if (mood && p.mood === mood) score += 2;
    const sharedInterests = interests.filter(i => p.interests.includes(i)).length;
    score += sharedInterests;
    return { persona: p, score };
  });
  scores.sort((a, b) => b.score - a.score);
  return scores[0].persona;
}

module.exports = { scoreMatch };
