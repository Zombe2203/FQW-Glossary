import React from "react";

import "./Relation.css"

interface IRelationProps {
  id: string;
  relation: string;
}

export const Relation: React.FC<IRelationProps> = ({
  id,
  relation
}) => {
  return (
    <div id={id} className="relation">
      {relation}
    </div>
  )
}