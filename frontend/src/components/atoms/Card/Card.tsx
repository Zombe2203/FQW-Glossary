import React from "react";

import { IGlossaryItem } from "../../../interfaces/glossary-item.interface";

import "./Card.css";


export const Card: React.FC<IGlossaryItem> = ({
  concept,
  definition,
  source
}) => {
  return (
    <div className="card">
      <div className="card-title">
        <p>{concept}</p>
      </div>

      <div className="card-definition">
        <p>{definition}</p>
      </div>

      <div className="card-definition">
        <p>{source}</p>
      </div>
    </div>
  )
}