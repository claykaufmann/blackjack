import * as React from 'react';
import Card from './Card';

const Player = (value, items) => {
  const cards = items;
  const playerVal = value;

  return (
    <>
      <p>Player hand value is {playerVal}</p>
      <ul>
        {cards.map((card) => (
          <li>
            <Card value={card.value} suit={card.suit} />
          </li>
        ))}
      </ul>
    </>
  );
};

export default Player;
