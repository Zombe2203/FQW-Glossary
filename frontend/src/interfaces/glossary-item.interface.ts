export interface IGlossaryItem {
  id: string;
  concept: string;
  definition: string;
  source?: string;
  childConcepts?: IChild[];
}

export interface IChild {
  child: string;
  connector: string;
}