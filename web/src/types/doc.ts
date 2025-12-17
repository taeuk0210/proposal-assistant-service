export type DocResponse = {
  id: number;
  user_id: number;
  title: string;
  url: string;
  size: number;
  created_at: Date;
};

export type DocListResponse = {
  items: DocResponse[];
  total: number;
};
