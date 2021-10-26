import http from 'http';
// game begins

// initial deal

const res = http.get('/api/initial_deal');

const data = JSON.parse(res);

playerCards = data.player.cards;

const playerInput = {
  player: {
    action: 'hit',
  },
  dealer: {
    action: 'stay',
  },
};

data = JSON.stringify(playerInput);

const res = http.post('/api/pass_action');