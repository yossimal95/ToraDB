USE [TorahDB]
GO
/****** Object:  Table [dbo].[CharacterAliases]    Script Date: 05/05/2026 11:57:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CharacterAliases](
	[AliasID] [int] IDENTITY(1,1) NOT NULL,
	[CharacterID] [int] NOT NULL,
	[AliasNameHe] [nvarchar](100) COLLATE Hebrew_CI_AS NOT NULL,
	[AliasNameEn] [nvarchar](100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
PRIMARY KEY CLUSTERED 
(
	[AliasID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Characters]    Script Date: 05/05/2026 11:57:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Characters](
	[CharacterID] [int] IDENTITY(1,1) NOT NULL,
	[MainNameHe] [nvarchar](100) COLLATE Hebrew_CI_AS NOT NULL,
	[MainNameEn] [nvarchar](100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	[FatherID] [int] NULL,
	[MotherID] [int] NULL,
	[AgeAtDeath] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[CharacterID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Marriages]    Script Date: 05/05/2026 11:57:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Marriages](
	[MarriageID] [int] IDENTITY(1,1) NOT NULL,
	[HusbandID] [int] NOT NULL,
	[WifeID] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[MarriageID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[CharacterAliases] ON 

INSERT [dbo].[CharacterAliases] ([AliasID], [CharacterID], [AliasNameHe], [AliasNameEn]) VALUES (1, 1, N'אדם הראשון', NULL)
INSERT [dbo].[CharacterAliases] ([AliasID], [CharacterID], [AliasNameHe], [AliasNameEn]) VALUES (2, 2, N'אם כל חי', NULL)
SET IDENTITY_INSERT [dbo].[CharacterAliases] OFF
GO
SET IDENTITY_INSERT [dbo].[Characters] ON 

INSERT [dbo].[Characters] ([CharacterID], [MainNameHe], [MainNameEn], [FatherID], [MotherID], [AgeAtDeath]) VALUES (1, N'אדם', N'Adam', NULL, NULL, 930)
INSERT [dbo].[Characters] ([CharacterID], [MainNameHe], [MainNameEn], [FatherID], [MotherID], [AgeAtDeath]) VALUES (2, N'חוה', N'Eve', NULL, NULL, NULL)
INSERT [dbo].[Characters] ([CharacterID], [MainNameHe], [MainNameEn], [FatherID], [MotherID], [AgeAtDeath]) VALUES (3, N'קין', N'Cain', 1, 2, NULL)
INSERT [dbo].[Characters] ([CharacterID], [MainNameHe], [MainNameEn], [FatherID], [MotherID], [AgeAtDeath]) VALUES (4, N'הבל', N'Abel', 1, 2, NULL)
INSERT [dbo].[Characters] ([CharacterID], [MainNameHe], [MainNameEn], [FatherID], [MotherID], [AgeAtDeath]) VALUES (5, N'שת', N'Seth', 1, 2, 912)
SET IDENTITY_INSERT [dbo].[Characters] OFF
GO
SET IDENTITY_INSERT [dbo].[Marriages] ON 

INSERT [dbo].[Marriages] ([MarriageID], [HusbandID], [WifeID]) VALUES (1, 1, 2)
SET IDENTITY_INSERT [dbo].[Marriages] OFF
GO
ALTER TABLE [dbo].[CharacterAliases]  WITH CHECK ADD  CONSTRAINT [FK_CharacterAlias] FOREIGN KEY([CharacterID])
REFERENCES [dbo].[Characters] ([CharacterID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[CharacterAliases] CHECK CONSTRAINT [FK_CharacterAlias]
GO
ALTER TABLE [dbo].[Characters]  WITH CHECK ADD  CONSTRAINT [FK_Father] FOREIGN KEY([FatherID])
REFERENCES [dbo].[Characters] ([CharacterID])
GO
ALTER TABLE [dbo].[Characters] CHECK CONSTRAINT [FK_Father]
GO
ALTER TABLE [dbo].[Characters]  WITH CHECK ADD  CONSTRAINT [FK_Mother] FOREIGN KEY([MotherID])
REFERENCES [dbo].[Characters] ([CharacterID])
GO
ALTER TABLE [dbo].[Characters] CHECK CONSTRAINT [FK_Mother]
GO
ALTER TABLE [dbo].[Marriages]  WITH CHECK ADD  CONSTRAINT [FK_Husband] FOREIGN KEY([HusbandID])
REFERENCES [dbo].[Characters] ([CharacterID])
GO
ALTER TABLE [dbo].[Marriages] CHECK CONSTRAINT [FK_Husband]
GO
ALTER TABLE [dbo].[Marriages]  WITH CHECK ADD  CONSTRAINT [FK_Wife] FOREIGN KEY([WifeID])
REFERENCES [dbo].[Characters] ([CharacterID])
GO
ALTER TABLE [dbo].[Marriages] CHECK CONSTRAINT [FK_Wife]
GO
