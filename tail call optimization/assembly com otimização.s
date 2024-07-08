	.file	"teste.c"
	.text
	.section .rdata,"dr"
LC0:
	.ascii "%llu \0"
	.text
	.p2align 4,,15
	.globl	_contar
	.def	_contar;	.scl	2;	.type	32;	.endef
_contar:
LFB13:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	pushl	%edi
	.cfi_def_cfa_offset 12
	.cfi_offset 7, -12
	pushl	%esi
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushl	%ebx
	.cfi_def_cfa_offset 20
	.cfi_offset 3, -20
	subl	$28, %esp
	.cfi_def_cfa_offset 48
	movl	48(%esp), %ebp
	movl	52(%esp), %ebx
	movl	56(%esp), %esi
	movl	60(%esp), %edi
	movl	%ebx, %eax
	cmpl	%esi, %ebp
	sbbl	%edi, %eax
	jc	L1
	.p2align 4,,10
L2:
	movl	%esi, 4(%esp)
	movl	%edi, 8(%esp)
	movl	$LC0, (%esp)
	call	_printf
	addl	$1, %esi
	movl	%ebx, %eax
	adcl	$0, %edi
	cmpl	%esi, %ebp
	sbbl	%edi, %eax
	jnc	L2
L1:
	addl	$28, %esp
	.cfi_def_cfa_offset 20
	popl	%ebx
	.cfi_restore 3
	.cfi_def_cfa_offset 16
	popl	%esi
	.cfi_restore 6
	.cfi_def_cfa_offset 12
	popl	%edi
	.cfi_restore 7
	.cfi_def_cfa_offset 8
	popl	%ebp
	.cfi_restore 5
	.cfi_def_cfa_offset 4
	ret
	.cfi_endproc
LFE13:
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC1:
	.ascii "\12\12Finalizou corretamente (=\0"
	.section	.text.startup,"x"
	.p2align 4,,15
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB14:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%edi
	.cfi_offset 7, -12
	xorl	%edi, %edi
	pushl	%esi
	.cfi_offset 6, -16
	xorl	%esi, %esi
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	.p2align 4,,10
L8:
	movl	%esi, 4(%esp)
	movl	%edi, 8(%esp)
	movl	$LC0, (%esp)
	call	_printf
	addl	$1, %esi
	adcl	$0, %edi
	movl	%esi, %eax
	xorl	$120001, %eax
	movl	%edi, %edx
	orl	%eax, %edx
	jne	L8
	movl	$LC1, (%esp)
	call	_puts
	movl	$0, (%esp)
	call	*__imp____acrt_iob_func
	movl	%eax, (%esp)
	call	_getc
	leal	-8(%ebp), %esp
	xorl	%eax, %eax
	popl	%esi
	.cfi_restore 6
	popl	%edi
	.cfi_restore 7
	popl	%ebp
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE14:
	.ident	"GCC: (i686-posix-dwarf-rev0, Built by MinGW-W64 project) 8.1.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
	.def	_puts;	.scl	2;	.type	32;	.endef
	.def	_getc;	.scl	2;	.type	32;	.endef
