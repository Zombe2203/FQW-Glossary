import { ICoordinate } from "./coordinates.interface";

export interface INode {
  current: ICoordinate;
  position: ICoordinate;
  relativePosition: ICoordinate;
  dragging: boolean;
}