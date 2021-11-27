import * as React from 'react';

const Card = (props) => {
  const data = props;
  const { value, suit, visibility } = data;

  let card = <></>;
  /* switch case for suits */
  // let cSuit = '';

  // switch(suit) {
  //   case 'Hearts':
  //     cSuit = <>&hearts</>;
  //     break;

  //   case 'Diamonds':
  //     cSuit = <>&diams</>;
  //     break;

  //   case 'Spades':
  //     cSuit = <>&spades</>;
  //     break;

  //   case 'Clubs':
  //     cSuit = <>&clubs</>;
  //     break;

  //   default:
  //     break;
  // }

  if (visibility === false) {
    card = (
      <>
        <p className="Card-backside" />
      </>
    );
  } else {
    card = (
      <>
        <div className="Card-front">
          <div className="Top-value"> {value} </div>
          <div className="Suit"> {suit} </div>
          <div className="Bottom-value"> {value} </div>
        </div>
      </>
    );
  }

  return <div className="Card">{card}</div>;
};

export default Card;
