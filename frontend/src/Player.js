import * as React from 'react';
import Card from './Card';

const Player = (value, cards) => {
  const items = cards;
  const playerVal = value;

  return (
    <>
      <p>Player hand value is {playerVal}</p>
      <ul>
        {items.map((card) => (
          <li>
            <Card value={card.value} suit={card.suit} />
          </li>
        ))}
      </ul>
    </>
  );
};

export default Player;
