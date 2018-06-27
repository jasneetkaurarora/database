CREATE TABLE [dbo].[tbl_Customer]
(
[Name] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Surname] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Telephone] [varchar] (20) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Address] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[ID] [int] NOT NULL IDENTITY(1, 1)
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[tbl_Customer] ADD CONSTRAINT [PK_tbl_Customer] PRIMARY KEY CLUSTERED  ([ID]) ON [PRIMARY]
GO
