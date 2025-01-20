import React, { FC, useEffect } from "react";

import { Relation } from "../../atoms/Relation/Relation";
import { NodeItem } from "../../atoms/NodeItem/NodeItem";

import { IGlossaryItem } from "../../../interfaces/glossary-item.interface";
import { ILink } from "../../../interfaces/link.interface";

import { coordinates } from "../../../resources/coordinates";

import "./Graf.css"

const getNodeCharacteristics = (id: string) => {
  const sourceNode = document.getElementById(`node-${id}`);

  const translate = sourceNode?.style.getPropertyValue("transform").match(/\d+/g);

  const width = sourceNode?.offsetWidth ?? 0;
  const height = sourceNode?.offsetHeight ?? 0;

  const translateX = Number(translate ? translate[0] : 0);
  const translateY = Number(translate ? translate[1] : 0);

  const left = Number(sourceNode?.clientLeft);
  const top = Number(sourceNode?.clientTop);

  return {
    width,
    height,
    translateX,
    translateY,
    left,
    top
  }
}

const connectNodes = (relations: ILink[]) => {
  const canvas = document.getElementById('canvas') as HTMLCanvasElement;
  const context = canvas?.getContext('2d');

  context?.clearRect(0, 0, canvas.width, canvas.height);

  relations.forEach(notionLink => {
    const {
      width: sourceWidth,
      height: sourceHeight,
      translateX: sourceTranslateX,
      translateY: sourceTranslateY,
      left: sourceLeft,
      top: sourceTop
    } = getNodeCharacteristics(notionLink.source);

    const {
      width: targetWidth,
      height: targetHeight,
      translateX: targetTranslateX,
      translateY: targetTranslateY,
      left: targetLeft,
      top: targetTop
    } = getNodeCharacteristics(notionLink.target);

    context?.beginPath()

    context?.moveTo(sourceWidth / 2 + sourceTranslateX + sourceLeft, sourceHeight / 2 + sourceTranslateY + sourceTop);

    context?.lineTo(targetWidth / 2 + targetTranslateX + targetLeft, targetHeight / 2 + targetTranslateY + targetTop)

    if (context?.lineWidth) {
      context.lineWidth = 2;
    }

    context?.stroke();

    const notionRelationTranslateX = (sourceWidth / 2 + sourceTranslateX + sourceLeft + targetWidth / 2 + targetTranslateX + targetLeft) / 2;
    const notionRelationTranslateY = (sourceHeight / 2 + sourceTranslateY + sourceTop + targetHeight / 2 + targetTranslateY + targetTop) / 2;

    const notionRelation = document.getElementById(`relation-${notionLink.source}-${notionLink.target}`);

    const notionRelationWidth = notionRelation?.offsetWidth ?? 0;
    const notionRelationHeight = notionRelation?.offsetHeight ?? 0;

    notionRelation?.style.setProperty("transform", `translate(${notionRelationTranslateX - notionRelationWidth / 2}px, ${notionRelationTranslateY - notionRelationHeight / 2}px)`);
  });
}

interface IGraf {
  concepts: IGlossaryItem[];
  relations: ILink[]
}

export const Graf: FC<IGraf> = ({ concepts, relations }) => {

  useEffect(() => {
    connectNodes(relations);
  }, []);

  return (
    <>
      <canvas
        className="container"
        id="canvas"
        width={window.innerWidth}
        height={window.innerHeight - 30}
      />

      {concepts.map((term, index) =>
        <NodeItem
          id={`node-${term.id}`}
          title={term.concept}
          connectNodes={connectNodes}
          relations={relations}
          initialPosition={{
            x: -coordinates[index].x,
            y: -coordinates[index].y
          }}
        />
      )}

      {relations.map(notionLink =>
        <Relation
          id={`relation-${notionLink.source}-${notionLink.target}`}
          relation={notionLink.relation}
        />
      )}
    </>
  );
}